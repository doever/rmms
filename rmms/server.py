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
from rmms import setting

from rmms.essay.view import test
test()

httpd = make_server(setting.HOST[0], setting.PORT, router.application)
print(f"Serving HTTP on port {setting.HOST[0]}:{setting.PORT}...")
print('please enter Ctrl+C to break...')
# 开始监听HTTP请求:
httpd.serve_forever()

