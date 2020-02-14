#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-14 15:19:12
# @Author  : 王若水 (wang_ruoshui@outlook.com)
# @Link    : http://example.org
# @Version : $Id$

'错误、调试'

from functools import reduce
from HSSBC import str2float
from GJTX import trim

def str2num(s):
    try:
        return int(s)
    except Exception as e:  # 别人家的代码：有内置函数(float)
        return str2float(trim(s))

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score<0 or self.score>100:
            raise ValueError('score must between 0 and 100')
        
        if self.score >= 80:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

if __name__ == '__main__':
    main()

