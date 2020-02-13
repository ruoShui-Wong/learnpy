#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-11 17:15:39
# @Author  : 王若水 (wang_ruoshui@outlook.com)
# @Link    : http://example.org
# @Version : $Id$


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

s = Student()
print(s.name)
print(s.score)      # 属性里没有该项
print(s.age())      # 方法里也没有该项


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


