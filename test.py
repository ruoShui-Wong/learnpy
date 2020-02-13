#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-11 17:15:39
# @Author  : 王若水 (wang_ruoshui@outlook.com)
# @Link    : http://example.org
# @Version : $Id$

class Screen(object):
    # 限制实例属性测试
    __slots__ = ('_width', '_height', '_resolution')

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width<100:
            raise ValueError('width is too low')
        self._width = width
    
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height


    @property
    def resolution(self):
        return self._height * self._width

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')