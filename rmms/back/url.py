#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/16 22:43'

import os
import sys

# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from rmms.back.view import *

url = [
        # sql页面
        ('/sql', sql),
        ('/run_sql', run_sql),
       ]


if __name__ == '__main__':
    pass

