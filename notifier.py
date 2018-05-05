# coding: utf-8

from pyfcm import FCMNotification
import settings
import json
import requests

API_KEY = settings.AP
DEVICE_REGISTRATION_ID = settings.DRI

class Notifier():
    def __init__(self):
        self.push_service = FCMNotification(api_key=API_KEY)
        self.registration_id = DEVICE_REGISTRATION_ID
    
    def notify(self, title, body, data):

        payload = {
            "to": "/topics/mytopic",
            "notification": {
            "title": title,
            "body" : body,
            "data" : data,
            "sound": "default",
            "vibrate": "true"
            },
            "data": {
                "title": title,
                "body" : body,
                "data" : data,
                "sound": "default",
                "vibrate": "true"
            },
            "priority": "high"
        }

        url = 'https://fcm.googleapis.com/fcm/send'
        headers = {'Authorization': 'key=' + API_KEY, 'content-type': 'application/json'}
        result = requests.post(url, data=json.dumps(payload), headers=headers)
        print(result)

if __name__=='__main__':
    notifier = Notifier()
    notifier.notify("title", "body", "data")
