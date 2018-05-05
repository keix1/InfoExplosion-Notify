# coding: utf-8

from news import twitterprovider

class News_Provider():
    def __init__(self):
        self.news = {}

    def get_news(self):
        self.news = twitterprovider.get_tweets()
        return self.news