#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: 0002.py
import mysql.connector
import random

loweraz = [chr(i) for i in range(ord("a"), ord("z")+1)]
upperaz = [chr(i) for i in range(ord("A"), ord("Z")+1)]
d09 = [chr(i) for i in range(ord("0"), ord("9")+1)]
wordbox = loweraz + upperaz + d09


def keys(maxnumber):
    n = 0
    while n < maxnumber:
        keystr = ''.join(random.sample(wordbox, 8))
        n = n + 1
        yield keystr

keylist = []
for k in keys(200):
    keylist.append(k)

keydict = dict()
for i in range(1, 201):
    keydict[i] = keylist[i-1]

conn = mysql.connector.connect(user='root', password='xxzx62100', database='arc', use_unicode=True)
cursor = conn.cursor()
cursor.execute('create table keydict (id int(20) primary key, keyvalue varchar(20))')

for key in keydict.keys():
    print [key, keydict[key]]
    cursor.execute('insert into keydict (id, keyvalue) values (%s, %s)', [key, keydict[key]])

print cursor.rowcount   # 这里为什么只影响了1行？
conn.commit()   # 妈的，开始把这个搞忘了调试了半天才找到原因！
cursor.close()
conn.close()

