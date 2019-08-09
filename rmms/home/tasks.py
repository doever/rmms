#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/9 22:33'

# import schedule
# import time
#
#
# def job():
#     print("I'm working...")
#
#
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).days.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)

import datetime
import schedule
import threading
import time


def job1():
    print("I'm working for job1")
    time.sleep(2)
    print("job1:", datetime.datetime.now())


def job2():
    print("I'm working for job2")
    time.sleep(2)
    print("job2:", datetime.datetime.now())


def job1_task():
    threading.Thread(target=job1).start()


def job2_task():
    threading.Thread(target=job2).start()


def run():
    schedule.every(10).seconds.do(job1_task)
    schedule.every(10).seconds.do(job2_task)

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == '__main__':
    run()