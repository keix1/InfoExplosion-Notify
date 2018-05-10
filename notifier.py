# coding: utf-8

import settings
import json
import requests

API_KEY = settings.AP

class Notifier():
    def notify(self, title, body, data):

        payload = {
            "to": "/topics/mytopic",
            "notification": {
            "title": title,
            "body" : body,
            "data" : data,
            "click_action": "InfoExplosion",
            "sound": "default",
            "vibrate": "true"
            },
            "data": {
                "title": title,
                "body": body,
                "data": data,
                "sound": "default",
                "vibrate": "true"
            },
            "android": {
                "priority": "high"
            },
            "webpush": {
                "headers": {
                    "Urgency": "high"
                }
            },
        }

        url = 'https://fcm.googleapis.com/fcm/send'
        headers = {'Authorization': 'key=' + API_KEY, 'content-type': 'application/json'}
        result = requests.post(url, data=json.dumps(payload), headers=headers)
        print(result)

if __name__=='__main__':
    notifier = Notifier()
    notifier.notify("title", "body", "data")
