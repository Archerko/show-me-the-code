#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: 0016.py
import re
import xlwt
import os

'''
务必保证当前目录下没有numbers.xls
因为python的xlwt库只能新建xls表单并处理，无法对现有xls表单进行修改
要修改请使用xlutils库
'''

if os.path.exists('numbers.xls'):
    raise IOError('numbers.xls is already existed')
else:
    with open('numbers.txt', 'r') as f:
        txt = f.read()

pattern = re.compile(u'\[(\d+),\s*(\d+),\s*(\d+)\]')
numbers_list = pattern.findall(txt)

wb = xlwt.Workbook(encoding='utf-8')
sh = wb.add_sheet('numbers', cell_overwrite_ok=True)
style = xlwt.XFStyle()    # 指定中文格式，不然会报错
font = xlwt.Font()
font.name = 'SimSun'    # 指定宋体
style.font = font

k = 0
for _numbers in numbers_list:
    i = 0
    for _numbers_attr in _numbers:
        sh.write(k, i, _numbers_attr)
        i += 1
    k += 1
wb.save('numbers.xls')

print 'Work is done.'
