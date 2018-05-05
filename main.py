# coding: utf-8

from notifier import Notifier
from time import sleep
from news import newsprovider

def main():
    notifier = Notifier()
    news_p = newsprovider.News_Provider()

    while(True):
        for info in news_p.get_news():
            title = "News"
            body = info['text']
            data = "データ"
            notifier.notify(title, body, data)
            print(title + "," + body + "," + data)
            sleep(1)

        sleep(20)

if __name__ == '__main__':
    main()