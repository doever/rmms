#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/10 10:36'

from essay.url import url as essay_url
from home.url import url as home_url

urls = essay_url + home_url


if __name__ == '__main__':
    print(essay_url)
