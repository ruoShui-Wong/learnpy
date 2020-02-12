#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-11 17:15:39
# @Author  : 王若水 (wang_ruoshui@outlook.com)
# @Link    : http://example.org
# @Version : $Id$

from HSSBC import by_score

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_score, reverse=True)
print(L2)