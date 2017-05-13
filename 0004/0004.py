#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: 0004.py.py
import string

f = open('''1.Harry Potter and the Sorcerer's Stone.txt''', 'r')
txt = f.read()
txt = txt.replace(string.punctuation, '').split()
print len(txt)
f.close()



