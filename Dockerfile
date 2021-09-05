FROM python:slim

RUN pip install -U pip && pip install --no-cache-dir\
  pysesame3[cognito]\
  requests

ARG USERID=1000

RUN useradd -u $USERID -m python

WORKDIR /home/python/src
COPY subscribe.py ./
USER python

CMD ["python", "-u", "subscribe.py"]
