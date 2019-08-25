#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/7 20:48'

import os
import re


import setting
from urls import urls
from tools import print_log, tprint
from rmms.https.request import Request
from rmms.https.handle_static import StaticHandle


def application(environ, start_response):
    '''请求的入口'''
    request = Request(environ)

    for i in range(len(urls)):
        if urls[i][0] == request.path:
            tprint(urls[i][0])
            res = urls[i][1](request)
            break
        else:
            continue
    else:
        res = StaticHandle(request.path)

    if not res:
        return error_404(start_response, request.path)

    code = res.get('code')
    content_type = res.get('content_type')
    content = res.get('content')
    cookie = res.get('cookie')
    if cookie:
        start_response(code, [('Content-Type', content_type), ('set-cookie', cookie)])
    elif request.cookie:
        start_response(code, [('Content-Type', content_type), ('set-cookie', request.cookie)])
    else:
        start_response(code, [('Content-Type', content_type)])

    if re.search('\.jpg', request.path.split("/")[-1]):
        return [bytes(content)]
    else:
        return [bytes(content, encoding="utf-8")]


def handle_static(path):
    ''''处理js、css文件'''
    static_file = setting.BASE_PATH
    file_path_li = path.split("/")
    for i in file_path_li:
        static_file = os.path.join(static_file, i)

    with open(static_file, 'r', encoding='UTF-8') as f:
        text = f.read()
        f.close()

    return text


def handle_image(path):
    image = setting.BASE_PATH
    path_li = path.split('/')
    for i in path_li:
        image = os.path.join(image, i)
    with open(image, 'rb') as f:
        content_byte = f.read()
        f.close()

    return content_byte


def error_404(start_response, path):
    mes = f"请求url地址错误,出错地址'{path}'"
    print_log(error_404.__name__, mes)
    start_response('404 not found', [('Content-Type', 'text/html')])
    return [bytes('<h1>404 the pages you request was stolen by the martians...</h1>', encoding="utf-8")]


if __name__ == '__main__':
    pass