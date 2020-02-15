#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-15 10:36:20
# @Author  : 王若水 (wang_ruoshui@outlook.com)
# @Link    : http://example.org
# @Version : $Id$

'IO编程：操作文件和目录'

import os

def findFille(ss, pwd='.'):
    # 当前目录下查找
    # print(r'当前搜索路径：%s' % pwd)
    
    for x in os.listdir(pwd):
        fx = os.path.join(pwd, x)

        if os.path.isfile(fx):
            if ss in x:
                print(fx)
        else:
            findFille(ss, fx)



if __name__ == '__main__':
    # 显示当前目录
    pwd = os.path.abspath('.')
    print(pwd)

