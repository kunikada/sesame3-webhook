# sesame3-webhook

Send SESAME3 status to specified url.

- [Sesame Web API](https://doc.candyhouse.co/ja/SesameAPI)
- [mochipon/pysesame3](https://github.com/mochipon/pysesame3)

## Usage

    docker run -it \
           -e POST_URL=https://example.com \
           -e SESAME_UUID=3DE4DE72-AAF9-25C1-8D0F-C9E019BB060C \
           -e SESAME_SECRET=a13d4b890111676ba8fb36ece7e94f7d \
           -e SESAME_API_KEY=M10YD4NKnP3BzIraDzINg9vcjOzEc2uP3DWb2HJn \
           --restart=always \
           -d kunikada/sesame3-webhook

### ENVIRONMENT VARIABLES

 * GET_URL : URL to get (GET or POST Required)
 * POST_URL : URL to post (GET or POST Required)
 * SESAME_UUID : UUID of SESAME (Required)
 * SESAME_SECRET : Private key from QR code (Required)
 * SESAME_API_KEY : API key on dashboard (Required)

## GET sample

{device_id} will be replaced by UUID  
{state} will be replaced with locked or unlocked

    https://example.com/?device={device_id}&status={state}

## POST sample

    {
      "device_id": "3DE4DE72-AAF9-25C1-8D0F-C9E019BB060C",
      "locked": true,
      "timestamp": "2021-04-08T15:26:37"
    }


