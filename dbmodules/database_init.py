# coding:utf-8

# Python 3.5.2 にて動作を確認
# sqlite3 標準モジュールをインポート
import sqlite3

# データベースファイルのパス
dbpath = 'sample_db.sqlite3'

# データベース接続とカーソル生成
connection = sqlite3.connect(dbpath)
# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
# connection.isolation_level = None
cursor = connection.cursor()

# エラー処理（例外処理）
try:
    # CREATE
    cursor.execute("DROP TABLE IF EXISTS sample")

    cursor.execute("CREATE TABLE IF NOT EXISTS keyword (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS tweetword (id INTEGER PRIMARY KEY, name TEXT, importance INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS published (id INTEGER PRIMARY KEY, name TEXT, url TEXT, summary TEXT)")

    cursor.execute("INSERT INTO keyword (name) VALUES ('ウェアラブル')")
    cursor.execute("INSERT INTO keyword (name) VALUES ('機械学習')")
    cursor.execute("INSERT INTO keyword (name) VALUES ('FPS')")
    cursor.execute("INSERT INTO keyword (name) VALUES ('SF')")
    cursor.execute("INSERT INTO keyword (name) VALUES ('恋愛')")
    cursor.execute("INSERT INTO keyword (name) VALUES ('アニメ')")
    cursor.execute("INSERT INTO keyword (name) VALUES ('おすすめ')")
    cursor.execute("INSERT INTO keyword (name) VALUES ('ガジェット')")
    cursor.execute("INSERT INTO tweetword (name, importance) VALUES ('ソニー', 2)")
    cursor.execute("INSERT INTO published (name, url) VALUES ('ソニーとボーズ、大人気で品薄のネックスピーカーを聞き比べ', 'http://ascii.jp/elem/000/001/663/1663482/')")


except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])

# 保存を実行（忘れると保存されないので注意）
connection.commit()

# 接続を閉じる
connection.close()