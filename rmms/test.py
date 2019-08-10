#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/10 19:41'

import os
import sys

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)

# print(locale.getpreferredencoding(False))

import sched, time

s = sched.scheduler(time.time, time.sleep)


def print_time(a='default'):
    print("From print_time", time.time(), a)


def print_some_times():
    print(time.time())
    s.enter(10, 1, print_time)
    s.enter(5, 2, print_time, argument=('positional',))
    s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
    s.run()
    print(time.time())

def handle_schedule():
    s.enter(3, 1, print_time)
    print(time.time())
    s.run()

while True:
    handle_schedule()