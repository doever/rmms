#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/11 12:24'

from rmms.basemodel import BaseModel
from rmms.setting import DATABASE


class Model(BaseModel):
    # def __init__(self, db):
    #     super()

    def __str__(self):
        return "essay model object"


db = Model(DATABASE.get("essay"))


if __name__ == '__main__':
    print(DATABASE.get("essay"))

