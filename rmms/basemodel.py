#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/11 11:58'

import sqlite3
from tools import print_log
from setting import DATABASE


class BaseModel(object):
    '''数据库基类，定义一些公共方法'''
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
        except Exception as err:
            print_log("execute_sql", "执行sql报错：" + str(err))
            # self.cursor.close()
            # self.conn.close()
        else:
            pass

    def select(self, sql):
        self.execute_sql(sql)
        rows = self.cursor.fetchall()
        return rows

    def update(self, sql):
        self.execute_sql(sql)
        self.conn.commit()

    def insert(self, sql):
        self.execute_sql(sql)
        self.conn.commit()

    def delete(self, sql):
        self.execute_sql(sql)
        self.conn.commit()


class Model(BaseModel):
    # def __init__(self, db):
    #     super()

    def __str__(self):
        return "essay model object"


class Field:
    def __init__(self, name, column_type, primary_key, default_value):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default_value = default_value


class StringField(Field):
    def __init__(self, name, column_type='varchar(100)', primary_key=False, default_value=None):
        super().__init__(name, column_type, primary_key, default_value)


class IntegerField(Field):
    def __init__(self, name, primary_key=False, default_value=0):
        super().__init__(name, 'int', primary_key, default_value)


db = Model(DATABASE.get("essay"))

if __name__ == '__main__':
    print_log('xxx', 'error')


