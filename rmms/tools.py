#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/10 12:17'

import sys
from urllib import parse

'''
定义一些常用的方法
'''


def url_decode(s):
    '''urlencode解码'''
    if s:
        d = "keys=" + s
        return parse.parse_qs(d)['keys'][0]
    return s


def print_log(function_name, error_message):
    '''
        # 错误日志打印格式
        # args  : function_name,error_message
        # return: None
    '''
    print(">" + "=" * 70 + "<")
    print(f"Error Method :{function_name}")
    print(f"Error Message:{error_message}")
    print(">" + "=" * 70 + "<")


def tprint(s):
    print("*" * 75)
    print(s)
    print("*" * 75)


def print_info(s):
    print("*" * 30 + "INFO" + "*" * 30 )
    print(s)
    print("*" * 30 + "INFO" + "*" * 30)


if __name__ == '__main__':
    print_log("main", "调用函数发送错误")




