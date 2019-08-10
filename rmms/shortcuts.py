#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/10 11:39'

import os
import re
import json
from urllib import parse
from io import StringIO

from rmms import setting
from rmms.tools import print_log


def renter(file_name, user="default", username="未登录"):
    file_path = setting.TEMPLATE_PATH
    try:
        app_name = file_name.split(":")[0]
        html_name = file_name.split(":")[1]
    except IndexError as err:
        print(f"render path is wrong:\n{file_name}")
    else:
        html = os.path.join(file_path, app_name, html_name)
        with open(html, 'r', encoding='utf-8') as fp:
            try:
                text = fp.read()
                text = text.replace("^user^", user)
                text = text.replace("^username^", username)
            except UnicodeDecodeError as err:
                print_log(renter.__name__, err)
            else:
                fp.close()
                return {
                    'code': "200 OK",
                    'content_type': 'text/html',
                    'content': text
                }


def json_response(data):
    return {
        'code': "200 OK",
        'content_type': 'json',
        'content': data
    }