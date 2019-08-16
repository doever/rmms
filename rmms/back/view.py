#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/16 22:43'

from rmms import restful
from rmms.shortcuts import renter, json_response
from rmms.essay.model import db


def sql(request):
    '''sql查询页面'''
    if request.method == "GET":
        return renter("back:sql.html")
    else:
        return renter("back:sql.html")


if __name__ == '__main__':
    pass
