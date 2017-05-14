#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: 0013.py
import urllib
import urllib2
import re

url = 'http://tieba.baidu.com/p/2166231880'
headers = {}

request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
html = response.read()


def cbk(a, b, c):
    per = 100.0 * a * b / c
    if per > 0:
        per = 100
    print '%.2f%%' % per

pattern = re.compile(r'class="BDE_Image" src="(http://imgsrc.baidu.com/forum/[a-zA-Z0-9%./=]+)"')
imgurl_list = pattern.findall(html)
for imgurl in imgurl_list:
    imgname = imgurl.split('/')[-1]
    local = 'C:\\Users\\Arc\\PycharmProjects\\show-me-the-code\\0013\\img\\' + imgname
    urllib.urlretrieve(imgurl, local, cbk)

