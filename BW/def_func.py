#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-11 18:03:46
# @Author  : 王若水 (wang_ruoshui@outlook.com)
# @Link    : http://example.org
# @Version : $Id$

import math

# 一元二次方程的解
def quadratic(a, b, c):
    delta = math.sqrt(b**2 - 4*a*c)
    x1 = (-b + delta) / (2*a)
    x2 = (-b - delta) / (2*a)

    return x1, x2


# 默认参数
def enroll(name, gender, age=6, city='贵阳'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


# 可变参数
def calc(*num):
    # 显示参数封装类型
    print(type(num))

    sum = 0
    for x in num:
        sum = sum + x

    return sum


# 关键字参数
def person(name, *, age=18, gender):
    print('name:', name, 'age:', age, 'gender:', gender)

# 关于命名关键字参数，若不使用字典作为函数输入，目前个人觉得可以先不用
# 不仅要求名字相同，还要求个数必须相等。


# 乘积计算练习
def product(*m):
    # 为空时报错
    if m==():
        raise TypeError('输入参数个数为空')

    ans = 1
    for d in m:
        ans = ans * d

    return ans


# 汉诺塔的移动
def move(n, a, b, c):
    if n==1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
