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
from rmms.utils.tools import print_log


def renter(file_name, content=None):
    file_path = setting.TEMPLATE_PATH
    res = {}
    try:
        app_name = file_name.split(":")[0]
        html_name = file_name.split(":")[1]
    except IndexError as err:
        print(f"render path is wrong:\n{file_name}")
    else:
        html = os.path.join(file_path, app_name, html_name)
        with open(html, 'r', encoding='utf-8') as fp:
            text = fp.read()
            fp.close()
            res = {
                'code': "200 OK",
                'content_type': 'text/html',
                'content': text
            }
            if isinstance(content, dict) and isinstance(content.get("cookie"), dict):
                res.update(content.get("cookie"))

    return res


def json_response(data):
    return {
        'code': "200 OK",
        'content_type': 'json',
        'content': json.dumps(data)             # {code:200,message="",data={}}
    }