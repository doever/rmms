#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/9 22:46'

from rmms import restful
from rmms.shortcuts import renter, json_response
from rmms.essay.model import db


def login(request):
    '''登录页面'''
    if request.method == "GET":
        return renter("essay:essay_detail.html")
    else:
        cookie = {
            "user": "cl",
            "username": "华盛顿",
        }
        return renter("essay:essay_detail.html", {"cookie": cookie})


def index(request):
    '''首页'''
    if request.method == "GET":
        return renter("essay:index.html")
    else:
        return renter("essay:essay_detail.html")


def essay_detail(request):
    '''文章详情页'''
    if request.method == "GET":
        return renter("essay:essay_detail.html")
    else:
        return renter("essay:essay_detail.html")


def pub_essay(request):
    '''发表文章'''
    if request.method == "GET":
        return renter("essay:essay_detail.html")
    else:
        return renter("essay:essay_detail.html")


if __name__ == '__main__':
    print("test ok!!")


