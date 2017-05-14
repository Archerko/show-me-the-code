#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: 0008.py
import HTMLParser


class MyHTMLParser(HTMLParser.HTMLParser):
    def handle_data(self,data):
        print data

parser = MyHTMLParser()
with open('1.html', 'r') as f:
    parser.feed(f.read())
