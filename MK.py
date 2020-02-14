#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-13 11:57:59
# @Author  : 王若水 (wang_ruoshui@outlook.com)
# @Link    : http://example.org
# @Version : $Id$

'模块章节学习代码'

__author__ = 'RUO'

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
