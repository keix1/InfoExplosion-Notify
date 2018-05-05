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
        data_message = {
            "title" : title,
            "body" : body,
            "data" : data,
        }
        payload = {}
        with open('send.json', encoding='utf-8') as f:
            payload = json.load(f)
        url = 'https://fcm.googleapis.com/fcm/send'
        headers = {'Authorization': 'key=' + API_KEY, 'content-type': 'application/json'}
        result = requests.post(url, data=json.dumps(payload), headers=headers)
        print(result)

if __name__=='__main__':
    notifier = Notifier()
    notifier.notify("title", "body", "data")
