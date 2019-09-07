#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/11 12:24'

from rmms.models.basemodel import BaseModel
from rmms.setting import DATABASE
from rmms.models.model import Model as DBModel
from rmms.models.model import IntegerField, StringField, CharField, TextField


class Model(BaseModel):

    def __str__(self):
        return "essay model object"


db = Model(DATABASE.get("essay"))
# id                     int                      n                      用户主键     PK
# username               varchar(50)              n                      用户名
# password               varchar(50)              n                      用户密码
# name                   varchar(50)              n                      用户姓名
# address                varchar(100)             y                      用户地址
# telephone              varchar(20)              n                      用户手机
# email                  varchar(20)              n                      用户邮箱
# avator                 varchar(50)              y                      用户头像
# user_level             char(1)                  n                      用户等级  0：黑铁  1：白银 2：黄金...
# user_status            char(1)                  n                      用户状态  0：锁定  1：有效
# is_superuser           char(1)                  n                      是否管理员 0:否  1：是
# create_date            datetime                 n                      创建日期
# last_date              datetime                 n                      最后登录日期
# extend1                int                      y                      扩展字段1
# extend2                int                      y                      扩展字段2
# extend3                varchar(50)              y                      扩展字段3
# extend4                varchar(50)              y                      扩展字段4
# extend5                varchar(200)             y                      扩展字段5


class User(DBModel):
    id = IntegerField('id')
    username = StringField(name='username', length=50)
    password = StringField(name='password', length=50)
    name = StringField(name='name', length=50)
    address = StringField(name='address', length=100)
    telephone = StringField(name='telephone', length=20)
    email = StringField(name='email', length=20)
    avator = StringField(name='avator', length=50)
    user_level = CharField(name='user_level', length=1)


if __name__ == '__main__':
    print(DATABASE.get("essay"))

