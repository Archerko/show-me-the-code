#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: 0011.py
with open('filtered_words.txt', 'r') as f:
    filtered_list = f.readlines()
filtered_list = ''.join(filtered_list).split('\n')
print filtered_list

inputword = raw_input('请输入一个词语：')
if inputword in filtered_list:
    print 'Freedom'
else:
    print 'Human Rights'
