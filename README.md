# sesame3-webhook

Send SESAME3 status to specified url. (HTTP Post)

- [Sesame Web API](https://doc.candyhouse.co/ja/SesameAPI)
- [mochipon/pysesame3](https://github.com/mochipon/pysesame3)

## Usage

    docker run -it \
           -e POST_URL=https://example.com \
           -e SESAME_UUID=3DE4DE72-AAF9-25C1-8D0F-C9E019BB060C \
           -e SESAME_SECRET=a13d4b890111676ba8fb36ece7e94f7d \
           -e SESAME_API_KEY=M10YD4NKnP3BzIraDzINg9vcjOzEc2uP3DWb2HJn \
           -e SESAME_CLIENT_ID=us-west-1:a145fc1a-d0a8-11eb-b8bc-0242ac130003 \
           -d kunikada/sesame3-webhook

### ENVIRONMENT VARIABLES

 * POST_URL : URL to post (Required)
 * SESAME_UUID : UUID of SESAME (Required)
 * SESAME_SECRET : Private key from QR code (Required)
 * SESAME_API_KEY : API key on dashboard (Required)
 * SESAME_CLIENT_ID : Client ID on dashboard (Required)

## Post sample

    {
      "device_id": "3DE4DE72-AAF9-25C1-8D0F-C9E019BB060C",
      "locked": true,
      "timestamp": "2021-04-08T15:26:37"
    }


