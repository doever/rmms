#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
测试sched库demo示例
'''
# class sched.scheduler(timefunc=time.monotonic, delayfunc=time.sleep)
# scheduler 类定义了一个调度事件的通用接口。 它需要两个函数来实际处理“外部世界” —— timefunc 应当不带参数地调用，
# 并返回一个数字（“时间”，可以为任意单位）。delayfunc 函数应当带一个参数调用，与 timefunc 的输出相兼容，并且应
# 当延迟其所指定的时间单位。 每个事件运行后还将调用 delayfunc 并传入参数 0 以允许其他线程有机会在多线程应用中运行
# 在 3.3 版更改: timefunc 和 delayfunc 参数是可选的；可以安全的在多线程环境中使用
# scheduler.cancel(event)
# 从队列中删除事件。 如果 event 不是当前队列中的事件，则此方法将引发 ValueError。
#
# scheduler.empty()
# 如果事件队列为空，则返回真值。


import sched
import time
from tkinter import messagebox as mes

s = sched.scheduler(time.time, time.sleep)


def print_time(a='default'):
    print("From print_time:", time.time(), a)


def print_some_times():
    print(time.time())
    s.enter(10, 1, print_time)
    s.enter(5, 1, print_time, argument=("positional",))
    s.enter(5, 1, print_time, kwargs={"a": "keyword"})
    s.run()
    print(time.time())


def job(tips):
    # mes.showinfo("你已经连续工作了两个小时")
    mes.showinfo("贴心提示", tips)


def run():
    s.enter(60*60*2, 1, job, argument=("你已经连续工作了两个小时了",))
    s.run()


if __name__ == '__main__':
    # print_some_times()

    while True:
        run()

