#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-12 08:29:12
# @Author  : 王若水 (wang_ruoshui@outlook.com)
# @Link    : http://example.org
# @Version : $Id$

# 切片学习
def trim(s):
    # 空字符串
    if s=='':
        return ''

    # 查找第一个不是空格的字符位置
    i1 = 0
    while 1:
        if s[i1]!=' ':
            break

        i1 = i1 + 1
        
        # 全部为空格
        if i1==len(s)-1:
            return ''
    
    # 查找最后一个不是空格的字符位置
    i2 = -1
    while 1:
        if s[i2]!=' ':
            break

        i2 = i2 - 1
    
    return s[i1:i2] + s[i2]

