#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-12 08:29:12
# @Author  : 王若水 (wang_ruoshui@outlook.com)
# @Link    : http://example.org
# @Version : $Id$

# 切片学习
def trim0(s):
    # 空字符串
    if s=='':
        return ''

    # 查找第一个不是空格的字符位置
    i1 = 0
    while 1:
        if s[i1]!=' ':
            break

        i1 = i1 + 1
        
        # 全部为空格
        if i1==len(s)-1:
            return ''
    
    # 查找最后一个不是空格的字符位置
    i2 = -1
    while 1:
        if s[i2]!=' ':
            break

        i2 = i2 - 1
    
    return s[i1:i2] + s[i2]

# 别人家的代码
# 你都没看题---->去除字符串首尾的空格
def trim(s):
    while s!='' and s[0]==' ':
        s = s[1:]

    while s!='' and s[-1]==' ':
        s = s[:-1]

    return s
    

# 循环
def findMinAndMax(L):
    if L==[]:
        return (None, None)

    x1 = L[0]
    x2 = L[0]
    for d in L:
        if x1>d:
            x1=d

        if x2<d:
            x2=d
    return x1, x2


# 斐波拉契数列
def fib0(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

# 生成器实现
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        
        a, b = b, a + b
        n = n + 1
    return 'done'


# 杨辉三角
def triangles0(n=13):
    a = [1]
    yield a

    a = [1, 1]
    yield a

    for r in range(2, n):
        b = [1, 1]
        for i in range(1, len(a)):
            b.insert(i, a[i-1] + a[i])
        
        a = b
        yield a

# 别人家的代码
def triangles():
    a = [1]

    # 生成器是一种迭代器，可以无限次循环
    # 所以呢？这里可以直接使用 `while True`
    while True:
        yield a

        a = [0] + a + [0]
        a = [a[:-1][i] + a[1:][i] for i in range(len(a)-1)]

