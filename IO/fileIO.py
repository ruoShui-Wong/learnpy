#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-14 21:49:36
# @Author  : 王若水 (wang_ruoshui@outlook.com)
# @Link    : http://example.org
# @Version : $Id$

# 文件读写
with open(r'../MK.py', 'r', encoding='utf-8') as f:
    L = f.readlines()
    for l in L:
        print(l.strip())  # 调用strip()去除行位的'\n'

from io import StringIO


# StringIO和BytesIO
print('\n')

f = StringIO('ruoShui\nWong')

'''
f.write('Hello')
f.write(' ')
f.write('GoodBye')

f.seek(3)   # 设置都的其实位置
print(f.read())
'''

while True:
    s = f.readline()
    if s=='':
        break

    print(s.strip())

