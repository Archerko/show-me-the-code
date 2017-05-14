#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: 0014.py
import re
import xlwt
import os

'''
务必保证当前目录下没有student.xls
因为python的xlwt库只能新建xls表单并处理，无法对现有xls表单进行修改
要修改请使用xlutils库
'''

if os.path.exists('student.xls'):
    raise IOError('student.xls is already existed')
else:
    with open('student.txt', 'r') as f:
        txt = f.read()

pattern = re.compile(u'"(\d+)":\["([\u4e00 -\u9fa5]+)",(\d+),(\d+),(\d+)\]')   # 为什么匹配中文那里没空格不行？
student_list = pattern.findall(txt)

wb = xlwt.Workbook(encoding='utf-8')
sh = wb.add_sheet('student', cell_overwrite_ok=True)
style = xlwt.XFStyle()    # 指定中文格式，不然会报错
font = xlwt.Font()
font.name = 'SimSun'    # 指定宋体
style.font = font

k = 0
for _student in student_list:
    i = 0
    for _student_attr in _student:
        sh.write(k, i, _student_attr)
        i += 1
    k += 1
wb.save('student.xls')

print 'Work is done.'
