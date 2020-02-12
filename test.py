#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-11 17:15:39
# @Author  : 王若水 (wang_ruoshui@outlook.com)
# @Link    : http://example.org
# @Version : $Id$

import time
from HSSBC import log

# 测试
@log('', 'a')
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

f = fast(11, 22)
print('f =', f)

