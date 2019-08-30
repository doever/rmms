#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/9 22:46'

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


from rmms.essay.view import *


url = [
        # 登录页面
        ('/login', login),
        # 注册
        ('/login', register),
        # 首页
        ('/essay_index', index),
        # 文章详情页
        ('/essay_detail', essay_detail),
        # 发布文章
        ('/pub_essay', pub_essay),
        # 用户主页
        ('/pub_essay', pub_essay),
        # 用户资料设置
        ('/user_info', user_info),
       ]

if __name__ == '__main__':
    pass

