#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: 0009.py
import re

f = open('1.html', 'r')
txt = f.read()

href = re.findall(u'href="([a-zA-Z0-9./\\-:]*)"', txt)
print href
