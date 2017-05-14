#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: 0012.py
import re

with open('filtered_words.txt', 'r') as f:
    filtered_list = f.readlines()
filtered_list = ''.join(filtered_list).split('\n')
print filtered_list

input_sent = raw_input('请输入一句话：')
for i in filtered_list:
    if i in input_sent:
        #  _split_sent = input_sent.split(i)
        #  input_sent = '**'.join(_split_sent)
        if re.match('[ \u4e00 -\u9fa5]+', i):  # 判断是否是中文，=None则没匹配到中文，说明是英文
            star = '*' * len(i)
        else:  # 中文情况下
            star = '*' * (len(i)/3)
        input_sent = input_sent.replace(i, star)
print input_sent
