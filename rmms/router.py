#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/7 20:48'


class Request():
    def __init__(self):
        self.method = ''
        self.Get = {}
        self.Post = {}


def application(environ, start_response):
    # for k, v in environ.items():
    #     print(k+":"+str(v))

    request = Request()
    request.method = environ.get('REQUEST_METHOD')
    request.path = environ.get('PATH_INFO')
    # 构造request get请求参数
    try:
        request.Get = dict([[i.split("=")[0], i.split("=")[1]] if i.split("=") else "-" for i in environ.get('QUERY_STRING').split("&")])
    except Exception as err:
        request.Get = {}
    # wsgi.input  QUERY_STRING
    # 构造request post请求参数

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']