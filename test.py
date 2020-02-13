#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-11 17:15:39
# @Author  : 王若水 (wang_ruoshui@outlook.com)
# @Link    : http://example.org
# @Version : $Id$

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
bart.print_score()

