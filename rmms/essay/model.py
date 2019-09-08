#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/11 12:24'

from rmms.models.basemodel import BaseModel
from rmms.setting import DATABASE
from rmms.models.model import Model as DBModel
from rmms.models.model import IntegerField, StringField, CharField, TextField, DateField


class Model(BaseModel):

    def __str__(self):
        return "essay model object"


db = Model(DATABASE.get("essay"))


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
    user_status = CharField(name='user_status', length=1)
    is_superuser = CharField(name='is_superuser', length=1)
    create_date = DateField(name='create_date')
    last_date = DateField(name='last_date')
    extend1 = IntegerField(name='extend1')
    extend2 = IntegerField(name='extend2')
    extend3 = StringField(name='extend3', length=50)
    extend4 = StringField(name='extend4', length=50)
    extend5 = StringField(name='extend5', length=200)


if __name__ == '__main__':
    print(DATABASE.get("essay"))

