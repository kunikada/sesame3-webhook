import os, time, json, requests
from datetime import datetime
from pprint import pprint

from pysesame3.auth import CognitoAuth, WebAPIAuth
from pysesame3.cloud import SesameCloud
from pysesame3.helper import CHSesame2MechStatus
from pysesame3.chsesame2 import CHSesame2


def callback(device: CHSesame2, status: CHSesame2MechStatus):
    obj = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "device_id": device.getDeviceUUID(),
        "locked": status.isInLockRange(),
    }
    pprint(obj)

    url = os.getenv("GET_URL")
    if url:
        url = url.replace("{device_id}", obj["device_id"]).replace("{state}", "locked" if obj["locked"] else "unlocked")
        print(url)
        response = requests.get(url)
        print(response)

    url = os.getenv("POST_URL")
    if url:
        print(url)
        headers = {"Content-Type": "application/json"}
        response = requests.post(url=url, data=json.dumps(obj), headers=headers)
        print(response)

def main():
    """
    We have use two different authentication methods.
    `CognitoAuth` is not available by default.
    If you want to use it, run `pip install pysesame3[cognito]` instead of `pip install pysesame3`.

    WebAPIAuth: (Common) Using the Web API.
    CognitoAuth: (Optional) Behave like a mobile app.
    """
    # auth = WebAPIAuth(apikey="API_KEY")
    auth = CognitoAuth(
        apikey=os.getenv("SESAME_API_KEY"),
        client_id=os.getenv("SESAME_CLIENT_ID"),
    )

    """
    By decoding the QR code generated by the official iOS/Android app,
    you can get the information you need.
    https://sesame-qr-reader.vercel.app/
    """
    your_key_uuid = os.getenv("SESAME_UUID")
    your_key_secret = os.getenv("SESAME_SECRET")

    device = CHSesame2(
        authenticator=auth, device_uuid=your_key_uuid, secret_key=your_key_secret
    )

    """
    As the name implies, `mechStatus` indicates the mechanical status of the key.
    https://doc.candyhouse.co/ja/reference#chsesameprotocolmechstatus

    Please note that `mechStatus` always queries the server for the latest status.
    Calling it too often would stress the service, which leads to rate limits
    and other restrictions.

    On the other hand, `getDeviceShadowStatus` does not query the server,
    but returns a **shadow** which is the status **stored in this library**.

    If you are operating the key only in this library, ideally,
    this shadow will be perfectly consistent with the actual state.
    """
    print("=" * 10)
    print("[Initial MechStatus]")
    print((str(device.mechStatus)))

    """
    The reality, however, is not so simple. The key must be manually operated.
    Biggest problem here is that the Candy House server will not return an error
    even if the request was not actually processed successfully.

    But if you are using `CognitoAuth`, you can achieve magic!
    The mobile app shows the status of the key in almost real time.
    In the same way, you can **subscribe** to `mechStatus`.
    """
    device.subscribeMechStatus(callback)

    while True:
        time.sleep(5)


if __name__ == "__main__":
    main()
