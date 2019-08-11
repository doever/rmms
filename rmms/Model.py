#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'doever'
__date__ = '2019/8/11 19:26'


import os
from queue import Queue
import sqlite3


class Pool(object):
    """一个数据库连接池"""

    def __init__(self, max_active=5, max_wait=None, init_size=0, db_type="SQLite3", **config):
        self.__freeConns = Queue(max_active)
        self.maxWait = max_wait
        self.db_type = db_type
        self.config = config
        if init_size > max_active:
            init_size = max_active
        for i in range(init_size):
            self.free(self._create_conn())

    def __del__(self):
        print("__del__ Pool..")
        self.release()

    def release(self):
        """释放资源，关闭池中的所有连接"""
        while self.__freeConns and not self.__freeConns.empty():
            con = self.get()
            con.release()
        self.__freeConns = None

    def _create_conn(self):
        """创建连接 """
        if self.db_type in dbcs:
            return dbcs[self.db_type](**self.config)

    def get(self, timeout=None):
        """获取一个连接
        @param timeout:超时时间
        """
        if timeout is None:
            timeout = self.maxWait
        conn = None
        if self.__freeConns.empty():  # 如果容器是空的，直接创建一个连接
            conn = self._create_conn()
        else:
            conn = self.__freeConns.get(timeout=timeout)
        conn.pool = self
        conn.row_factory = sqlite3.Row
        return conn

    def free(self, conn):
        """将一个连接放回池中
        @param conn: 连接对象
        """
        conn.pool = None
        if self.__freeConns.full():  # 如果当前连接池已满，直接关闭连接
            conn.release()
            return
        self.__freeConns.put_nowait(conn)


class PoolingConnection(object):
    # __metaclass__ = ABCMeta

    def __init__(self, **config):
        self.conn = None
        self.config = config
        self.pool = None

    def __del__(self):
        self.release()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def release(self):
        print("release PoolingConnection..")
        if self.conn is not None:
            self.conn.close()
            self.conn = None
        self.pool = None

    def close(self):
        if self.pool is None:
            # raise PoolException("连接已关闭")
            raise Exception("连接已关闭")
        self.pool.free(self)

    def __getattr__(self, val):
        if self.conn is None and self.pool is not None:
            self.conn = self._create_conn(**self.config)
        if self.conn is None:
            # raise PoolException("无法创建数据库连接或连接已关闭")
            raise Exception("无法创建数据库连接或连接已关闭")
        return getattr(self.conn, val)

    # 定义一个抽象方法，该方法只有在子类中实例化才生效
    @abstractmethod
    def _create_conn(self, **config):
        pass


class SQLit3PoolConnection(PoolingConnection):
    def _create_conn(self, **config):
        conn = sqlite3.connect(**config)
        conn.row_factory = sqlite3.Row
        return conn


dbcs = {"SQLite3": SQLit3PoolConnection}

pool = Pool(database=os.path.join(os.path.abspath(__file__), "base.db3"))

