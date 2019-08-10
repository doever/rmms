#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/10 10:17'


import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOST = ['127.0.0.1']
PORT = 8088

TEMPLATE_PATH = os.path.join(BASE_PATH, 'templates')


# JS_PATH = os.path.join(BASE_PATH, 'js').replace("\\","/")
# CSS_PATH = os.path.join(BASE_PATH, 'css').replace("\\","/")
# IMAGE_PATH = os.path.join(BASE_PATH, 'images').replace("\\","/")
IMAGE_FORMAT = ['jpg', 'png']

if __name__ == '__main__':
    print(BASE_PATH)
