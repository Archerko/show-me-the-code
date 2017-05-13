#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: 0006.py
import collections
import re

f = open('''1.Harry Potter and the Sorcerer's Stone.txt''', 'r')
txt = f.read().lower()
word = re.findall('\w+-?\w*-?\w*-?\w*-?\w*-?\w*', txt)
print len(word)
print collections.Counter(word).most_common(10)  # Counter的参数是一个list，如果放入一个字符串，则把字符串当作了单独字符组成的list
f.close()
