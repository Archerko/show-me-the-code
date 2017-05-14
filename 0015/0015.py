#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: 0015.py
import re
import xlwt
import os

'''
city.xls
因为python的xlwt库只能新建xls表单并处理，无法对现有xls表单进行修改
要修改请使用xlutils库
'''

if os.path.exists('city.xls'):
    raise IOError('city.xls is already existed')
else:
    with open('city.txt', 'r') as f:
        txt = f.read()

pattern = re.compile(u'"(\d+)"\s*:\s*"([\u4e00 -\u9fa5]+)"')   # 为什么匹配中文那里没空格不行？
city_list = pattern.findall(txt)

wb = xlwt.Workbook(encoding='utf-8')
sh = wb.add_sheet('city', cell_overwrite_ok=True)
style = xlwt.XFStyle()    # 指定中文格式，不然会报错
font = xlwt.Font()
font.name = 'SimSun'    # 指定宋体
style.font = font

k = 0
for _city in city_list:
    i = 0
    for _city_attr in _city:
        sh.write(k, i, _city_attr)
        i += 1
    k += 1
wb.save('city.xls')

print 'Work is done.'
