# coding: utf-8
import json
import settings
from requests_oauthlib import OAuth1Session

CK = settings.TW_CS
CS = settings.TW_CS_SEC
AT = settings.TW_TK
ATS = settings.TW_TK_SEC
twitter = OAuth1Session(CK, CS, AT, ATS)

def get_tweets():
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params ={'count' : 10}
    req = twitter.get(url, params = params)

    if req.status_code == 200:
        timeline = json.loads(req.text)
        for tweet in timeline:
            print(tweet['user']['name']+'::'+tweet['text'])
            print(tweet['created_at'])
            print('----------------------------------------------------')
        return timeline
    else:
        print("ERROR: %d" % req.status_code)