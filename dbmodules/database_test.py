# coding:utf-8

from database import DatabaseController

dc = DatabaseController()

# print(dc.get_all_keyword("keyword"))
for i in dc.get_all_keyword("keyword"):
    print(i[1])

