#!/usr/bin/python3
# -*- coding:utf-8 -*-
import time


def how_mach_time(f):
    def wrapper(name):
        t1 = time.time()
        res = f(name)
        t2 = time.time()
        print("执行函数花费了%s秒！！" % str(t2-t1))
        return res
    print("222")
    return wrapper


@how_mach_time
def test(name):
    print("I am %s" % name)
    time.sleep(3)
    return "test function return value"
# test == how_much_time(test) == wapper
#  test() == how_much_time(test)() == wrapper()


if __name__ == '__main__':
    # 因为相当于how_much_time(test)  输出：222
    # a = test
    res = test("doever")
    print(res)
