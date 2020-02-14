#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-14 07:49:05
# @Author  : 王若水 (wang_ruoshui@outlook.com)
# @Link    : http://example.org
# @Version : $Id$

'面向对象高级编程'

# 定制类
# __iter__
class Fib(object):
    """斐波那契数列"""
    def __init__(self):
        self.a, self.b = 0, 1   # 初始化两个计数器a, b

    def __iter__(self):
        return self             # 需要返回的迭代对象就是本身

    def __next__(self):
        self.a, self.b = self.b, self.a+self.b

        if self.a>=23:
            raise StopIteration('迭代终止')

        return self.a           # 返回下一个值

# 打印数列
fib = Fib()
for n in fib:
    print(n)

