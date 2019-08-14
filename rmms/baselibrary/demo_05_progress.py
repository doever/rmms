#!/usr/bin/python3
# -*- coding:utf-8 -*-

from multiprocessing import Process
import time
import os


def run_proc(name):
    print("Run child process %s (%s)..." % (name, os.getpid()))


if __name__ == '__main__':
    print("Parent process %s" % os.getpid())
    time.sleep(5)
    p = Process(target=run_proc, args=("test",))
    print("Child process will start.")
    p.start()
    p.join()
    time.sleep(1)
    print("Child process end.")
