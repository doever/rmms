#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/7 20:49'


import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# import router.application
from rmms import router

httpd = make_server('', 8000, router.application)
print('Serving HTTP on port 8000...')
print('please enter Ctrl+C to break...')
# 开始监听HTTP请求:
httpd.serve_forever()

