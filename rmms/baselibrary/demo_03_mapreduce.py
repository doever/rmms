#!/usr/bin/python3
# -*- coding:utf-8 -*-


from functools import reduce


def _pow(_x):
    '''用于map测试'''
    return _x*_x


def _add(_x, _y):
    '''用于reduce测试'''
    return _x + _y


def test_map():
    '''map接受两个参数，将第二个参数(可迭代对象)依次作用在function上
        @:param(function name, iterable)
    '''
    r = map(_pow, [1, 2, 3, 4, 5])
    print(list(r))
    r1 = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(r1)


def test_reduce():
    '''reduce接受两个参数，reduce把一个函数作用在一个序列上，这个函数
       必须接收两个参数，reduce把序列前两个元素的函数作用结果继续和序
       列的下一个元素做累积计算
        @:param(function name, iterable)
    '''
    r = reduce(_add, [i for i in range(101)])
    print(r)


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(_s):
    '''字符串转换int'''
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    r = reduce(fn, map(char2num, _s))
    print(r)
    return r


if __name__ == '__main__':
    print("_" * 35 + "分界线" + "_" * 35)
    test_map()
    print("_" * 35 + "分界线" + "_" * 35)
    test_reduce()
    print("_" * 35 + "分界线" + "_" * 35)
    str2int("13456")
