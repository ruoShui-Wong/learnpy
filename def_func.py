#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-11 18:03:46
# @Author  : 王若水 (wang_ruoshui@outlook.com)
# @Link    : http://example.org
# @Version : $Id$

import math

def quadratic(a, b, c):
    delta = math.sqrt(b**2 - 4*a*c)
    x1 = (-b + delta) / (2*a)
    x2 = (-b - delta) / (2*a)

    return x1, x2


# 汉诺塔的移动
def move(n, a, b, c):
    if n==1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
