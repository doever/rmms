#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/9 22:46'

import time
from datetime import datetime

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
        return renter("essay:pub_essay.html")
    else:
        title = request.POST.get('title')
        category = request.POST.get('category')
        thumbnail = request.POST.get('thumbnail')
        content = request.POST.get('content')
        way = request.POST.get('way')
        author = request.POST.get('author')
        # 后期增加form模块过滤
        id = int(time.time())
        userid = request.user.get('userid')
        date = str(datetime.now())[0:19]
        db.insert(f"insert into essay values({id},{userid},'{thumbnail}','{title}','{content}','{category}',100,0,100,'1','{date}',0,0,'','','')")
        return restful.ok(message=id)


def user_info(request):
    '''用户资料设置'''
    if request.method == "GET":
        return renter("essay:user_info.html")
    else:
        pass


if __name__ == '__main__':
    print("test ok!!")


