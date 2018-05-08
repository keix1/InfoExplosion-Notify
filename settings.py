import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname('__file__'), '.env')
load_dotenv(dotenv_path)

# FCM
AP=os.environ.get("API_KEY")
DRI=os.environ.get("DEVICE_REGISTRATION_ID")

# Twitter
TW_CS=os.environ.get("TWITTER_CONSUMER_KEY")
TW_CS_SEC=os.environ.get("TWITTER_CONSUMER_SECRET")
TW_TK=os.environ.get("TWITTER_ACCESS_TOKEN")
TW_TK_SEC=os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
