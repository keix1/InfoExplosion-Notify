#coding: utf-8

from news import twitterprovider
from dbmodules import database
import random
from search.googlesearch import GoogleSearch
from notifier import Notifier
import time


def main():
    while True:
        try:
            notifier = Notifier()
            dc = database.DatabaseController()

            tweets = twitterprovider.get_tweets()
            keywords = []
            for row in dc.get_all_keyword():
                keywords.append(row[1])

            tweet = random.choice(tweets)['text']
            keyword = random.choice(keywords)

            print(tweet, keyword)

            gs = GoogleSearch()
            search_word = tweet + " " + keyword
            gs.search(search_word)
            gs.view()
            result_title = random.choice(gs.get_articles())[0]
            result_url = random.choice(gs.get_articles())[1]
            print(result_title)

            notifier.notify(title=search_word, body=result_title, data=result_url)
            time.sleep(60 * 20)
        except Exception as e:
            pass


if __name__=='__main__':
    main()

