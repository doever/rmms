#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
参考：https://www.jianshu.com/p/82008ba6706e
'''

import time
from datetime import date
from datetime import time as dtime
from datetime import timezone
from datetime import datetime
from datetime import timedelta


# __________________________________________date____________________________________________________
now = date.today()
# 构造方法
print(date(1994, 6, 2))
# 格式化时间戳为日期
print(date.fromtimestamp(time.time()))
# 从公元1年1月1日开始计算
print(date.fromordinal(100))
# 当前天
print(date.today())
# 星期几
print(date.weekday(now))
# 通用格式时间
print(date.ctime(now))
# 格式化日期
print(date.strftime(now, "%Y/%m/%d"))

# __________________________________________time____________________________________________________

# ________________________________________datetime__________________________________________________

# ________________________________________timezone__________________________________________________

# ________________________________________timedelta__________________________________________________
d = timedelta(microseconds=-1)
print((d.days, d.seconds, d.microseconds))

if __name__ == '__main__':
    pass
