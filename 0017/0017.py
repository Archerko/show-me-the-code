#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: 0017.py
import codecs
import xlrd

student = xlrd.open_workbook('student.xls')
sh = student.sheet_by_index(0)   # 获取第一张表

xml = list()
xml.append(u'<?xml version="1.0" encoding="UTF-8"?>\n')   # 一个'\'才是对的，表示转义
xml.append(u'<root>\n')
xml.append(u'<students>\n')
xml.append(u'<!-- \n')
xml.append(u'	学生信息表\n')
xml.append(u'	"id" : [名字, 数学, 语文, 英文]\n')
xml.append(u'-->\n')
xml.append(u'{\n')
for i in range(sh.nrows):
    _student = list()
    for k in range(sh.ncols):
        _student.append(sh.cell_value(i, k))
    if i == sh.nrows - 1:  # 判断是否最后一行
        xml.append(u'	"%s" : ["%s", %s, %s, %s]\n' % tuple(_student))
    else:
        xml.append(u'	"%s" : ["%s", %s, %s, %s],\n' % tuple(_student))
xml.append(u'}\n')
xml.append(u'</students>\n')
xml.append(u'</root>\n')
xml = ''.join(xml)   # join函数中，不允许str和unicode混合join，所以上面的全部要换成unicode编码
with codecs.open('student.xml', 'w', 'utf-8') as f:    # 默认的open只能打开ascii码的文件，所以要用codecs模块里的open
    f.write(xml)

