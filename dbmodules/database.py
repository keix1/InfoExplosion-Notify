# coding: utf-8

import sqlite3
import os

class DatabaseController():

    def __init__(self, dbpath=os.path.dirname(os.path.abspath(__file__)) + "/sample_db.sqlite3"):
        self.connection = sqlite3.connect(dbpath)
        # 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
        # connection.isolation_level = None
        self.cursor = self.connection.cursor()

    def insert_keyword(self, name="name"):
        try:
            self.cursor.execute("INSERT INTO keyword (name) VALUES ('" + name + "')")

            self.cursor.execute("INSERT INTO tweetword (name, importance) VALUES ('ソニー', 2)")
            self.cursor.execute(
                "INSERT INTO published (name, url) VALUES ('ソニーとボーズ、大人気で品薄のネックスピーカーを聞き比べ', 'http://ascii.jp/elem/000/001/663/1663482/')")

        except sqlite3.Error as e:
            print('sqlite3.Error occurred:', e.args[0])

        # 保存を実行（忘れると保存されないので注意）
        self.connection.commit()

    def insert_tweetword(self, name="name", importance=0):
        try:
            self.cursor.execute("INSERT INTO tweetword (name, importance) VALUES ('" + name + "', " + importance + ")")
        except sqlite3.Error as e:
            print('sqlite3.Error occurred:', e.args[0])

        # 保存を実行（忘れると保存されないので注意）
        self.connection.commit()

    def insert_keyword(self, name="name", url="http://google.com"):
        try:
            self.cursor.execute("INSERT INTO published (name, url) VALUES ('" + name + "', '" + url + "')")

        except sqlite3.Error as e:
            print('sqlite3.Error occurred:', e.args[0])

        # 保存を実行（忘れると保存されないので注意）
        self.connection.commit()

    def get_all_keyword(self, database="keyword"):
        return self.cursor.execute("SELECT * FROM " + database)

    def close(self):
        # 接続を閉じる
        self.connection.close()


