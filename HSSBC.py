#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-12 15:15:44
# @Author  : 王若水 (wang_ruoshui@outlook.com)
# @Link    : http://example.org
# @Version : $Id$

from functools import reduce

# 高阶函数：map/reduce
# eg1
def normalize(name):
    return name[0].upper() + name[1:].lower()

# eg2
def prod(L):
    return reduce(lambda x, y: x*y, L)

# eg3
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2float(s):
    # 整数部分和小数部分拆分：别人家的代码，直接使用`split`函数分割得s1、s2
    for i in range(1, len(s)):
        if s[i] == '.':
            break

    s1 = s[:i]
    s2 = s[-1:i:-1]

    f0 = reduce(lambda x, y: x * 10 + y, map(char2num, s1));
    f1 = reduce(lambda x, y: x / 10 + y, map(char2num, s2));
    return f0 + f1/10
