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

    # 迭代功能
    def __iter__(self):
        return self             # 需要返回的迭代对象就是本身

    def __next__(self):
        self.a, self.b = self.b, self.a+self.b

        if self.a>=81:
            raise StopIteration('迭代终止')

        return self.a           # 返回下一个值

    # 按下标取数
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 0, 1
            for x in range(n):
                a, b = b, a+b
            return a
        elif isinstance(n, slice):  # n是切片
            start = n.start
            stop  = n.stop
            if start is None:
                start = 1

            L = []
            a, b = 1, 1
            for x in range(1, stop):
                if x>=start:
                    L.append(a)
                a, b = b, a+b
            return L

'''
# 打印数列
fib = Fib()
for n in fib:
    print(n)

print('fib[5] =', fib[5])
print('fib[6] =', fib[6])
print('fib[7] =', fib[7])
print('fib[:8] =', fib[:8])
'''

# __str__
class Student(object):
    """docstring for Student"""
    def __init__(self, name='Rui'):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

    def __call__(self, X):
        print('my name is: %s %s' % (self.name, X))

    def __getattr__(self, name):
        if name=='score':
            return 99
        elif name == 'age':
            return lambda : 23
        else:
            raise AttributeError('No this attribute.')

'''
s = Student()
print(s.name)
print(s.score)      # 属性里没有该项
print(s.age())      # 方法里也没有该项
'''

# __getattr__
class Chain(object):
    N = 0

    def __init__(self, path=''):
        self.path = path

    def __getattr__(self, path):
        Chain.N += 1
        print(Chain.N)

        return Chain('%s/%s' % (self.path, path))

    def __str__(self):
        return self.path

    __repr__ = __str__

s = Chain().www.baidu.com   # 多次重复创建实例
print(type(s))              # s仍是一个Chain实例
print(s)                    # 由于__str__函数，打印出来的东西有变

s0 = Chain()
s1 = s0.www
print(s1.path)
s2 = s1.baidu
print(s2.path)
s3 = s2.com
print(s3.path)

