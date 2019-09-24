#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/16 22:43'

from rmms.https import restful
from rmms.https.shortcuts import renter, json_response
from rmms.models.basemodel import db
from rmms.utils.tools import print_info


def sql(request):
    '''sql查询页面'''
    if request.method == "GET":
        return renter("back:sql.html")
    else:
        return renter("back:sql.html")


def run_sql(request):
    '''sql检查运行页面'''
    if request.method == "GET":
        pass
    else:
        action = request.POST.get("action")
        sql = request.POST.get("sql")
        # print_info(action)
        # print_info(sql)
        if action == "check":
            # 检查sql
            try:
                res = db.cursor.execute(sql)
            except Exception:
                return restful.server_error(message="SQL语法有误")
            else:
                return restful.ok(message="SQL语法检查成功")
        else:
            # 运行sql
            sql_type = sql.strip()[0:6]
            try:
                db.cursor.execute(sql)
            except:
                return restful.server_error(message="执行语句发生错误")
            else:
                if sql_type == "select":
                    res = db.cursor.fetchall()
                    cols_li = [col[0] for col in db.cursor.description]
                    return restful.ok(data={
                                            "res": res,
                                            "cols": cols_li
                                            })
                else:
                    db.conn.commit()
                    return restful.ok(message="语句执行成功")


if __name__ == '__main__':
    pass
