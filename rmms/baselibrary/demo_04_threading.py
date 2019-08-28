#!/usr/bin/python3
# -*- coding:utf-8 -*-
import threading
import time
from datetime import datetime


def print_thread():
    for i in range(3):
        print("正在输出...")
        time.sleep(1)


def draw_thread():
    for i in range(3):
        print("正在画画...")
        time.sleep(1)


def how_mach_time(f):
    def wrapper():
        t1 = time.time()
        res = f()
        t2 = time.time()
        print("执行函数共花费%s秒" % str(t2-t1))
        return res
    return wrapper


# @how_mach_time
def thread_run():
    time1 = time.time()
    t1 = threading.Thread(target=print_thread)
    t2 = threading.Thread(target=draw_thread)
    t1.start()
    t2.start()
    time2 = time.time()
    print(time2-time1)


@how_mach_time
def normal_run():
    print_thread()
    draw_thread()


if __name__ == '__main__':
    print("使用多线程调用方法：")
    thread_run()
    # print("使用单线程调用方法：")
    # normal_run()
