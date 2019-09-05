#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
日志模块
参考：https://cloud.tencent.com/developer/article/1354396
     https://www.jianshu.com/p/26849de20a83
'''
import logging


# _____________________________示例代码1__________________________________
# logging.basicConfig()
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


# _____________________________示例代码2__________________________________
# logging.basicConfig(filename="demo_09_logging.log", filemode="a", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


# _____________________________示例代码3__________________________________
logging.basicConfig(filename="test.log", filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
a, b = 5, 0
try:
    c = a / b
except Exception as e:
    # 当发生异常时，直接使用无参数的 debug()、info()、warning()、error()、critical() 方法并不能记录异常信息
    # 下面三种方式三选一，推荐使用第一种
    logging.exception("Exception occurred")
    logging.error("Exception occurred", exc_info=True)
    logging.log(level=logging.DEBUG, msg="Exception occurred", exc_info=True)


# _____________________________示例代码4__________________________________



if __name__ == '__main__':
    pass
