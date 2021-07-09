FROM python:slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    patch \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip && pip install --no-cache-dir\
  pysesame3[cognito]\
  requests

ARG USERID=1000

RUN useradd -u $USERID -m python

WORKDIR /home/python/src
COPY subscribe.py patchfile ./
RUN patch /usr/local/lib/python3.9/site-packages/pysesame3/chsesame2.py patchfile
USER python

CMD ["python", "-u", "subscribe.py"]
