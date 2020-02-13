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
        return lambda: 7

s = Student()
s('Shui')
print(s.name)



class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

c = Chain().status.user.timeline.list
print(c)


