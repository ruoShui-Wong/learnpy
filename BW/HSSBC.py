#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-12 15:15:44
# @Author  : 王若水 (wang_ruoshui@outlook.com)
# @Link    : http://example.org
# @Version : $Id$

# 高阶函数：map/reduce
from functools import reduce

# eg1
def normalize(name):
    return name[0].upper() + name[1:].lower()

# eg2
def prod(L):
    return reduce(lambda x, y: x*y, L)

# eg3
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2float(s):
    # 整数部分和小数部分拆分：别人家的代码，直接使用`split`函数分割得s1、s2
    for i in range(1, len(s)):
        if s[i] == '.':
            break

    s1 = s[:i]
    s2 = s[-1:i:-1]

    f0 = reduce(lambda x, y: x * 10 + y, map(char2num, s1));
    f1 = reduce(lambda x, y: x / 10 + y, map(char2num, s2));
    return f0 + f1/10


# filter
# 素数生成
# 1. 奇数序列生成器
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 2. 筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0

# 3. 素数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 回数
def is_palindrome(n):
    s = str(n)

    return s[:] == s[::-1]


# sorted
# 想办法把用于排序的那个变量取出来就可以了
def by_score(t):
    return t[1]



# 返回函数
def createCounter():
    n = [0]         # 列表对象才是可以变的
    def counter():
        n[0] += 1
        return n[0]

    return counter



# 装饰器
from functools import wraps
from time import time

def log(*text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            print('your input is:', text)
            print('begin call function \'%s\'' % func.__name__)
            t0 = time()
            ans = func(*args, **kw)
            t1 = time()
            print('end call')
            print('%.4fs elapsed' % (t1-t0))

            return ans

        return wrapper

    return decorator

