#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/9 22:46'

from rmms import restful
from rmms.shortcuts import renter, json_response


def index(request):
    '''首页'''
    if request.method == "GET":
        return renter("essay:essay_detail.html")
    else:
        return ''


def essay_detail(request):
    '''文章详情页'''
    if request.method == "GET":
        return ''
    else:
        return ''

def test():
    print("test ok!!")



if __name__ == '__main__':
    test()


