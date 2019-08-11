#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/9 22:46'

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


from rmms.essay.view import *


url = [
        # 首页
        ('/index', index),
        # 登录页面
        ('/login', index),
       ]

if __name__ == '__main__':
    pass

