#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: 0001.py
import random

loweraz = [chr(i) for i in range(ord("a"), ord("z")+1)]
upperaz = [chr(i) for i in range(ord("A"), ord("Z")+1)]
d09 = [chr(i) for i in range(ord("0"), ord("9")+1)]
wordbox = loweraz + upperaz + d09


def keys(maxnumber):
    n = 0
    while n < maxnumber:
        key = ''.join(random.sample(wordbox, 8))
        n = n + 1
        yield key

for i in keys(200):
    print i
