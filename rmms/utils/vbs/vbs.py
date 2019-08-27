#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/27 20:44'
import os


class Vbs():
    def __init__(self):
        pass

    def xls2csv(self, _src_file, _dist_file):
        if _dist_file[-3:0] != "csv":
            raise ValueError("目标文件不是csv类型")
        else:
            command = f"XlsToCsv.vbs {_src_file} {_dist_file}"
            os.system(command)


if __name__ == '__main__':
    pass
