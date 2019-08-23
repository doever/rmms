import os
import re

from rmms import setting
from rmms.https.response import ResponseBase


class StaticHandle(dict):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.code = '200 OK'
        self.content_type = ''
        self.content = ''

    def _handle(self):
        file_name = self.path.split("/")
        if re.search('\.css', file_name):
            self.content_type = 'text/css'
            self.handle_static()
        elif re.search('\.js', file_name):
            self.content_type = 'application/x-javascript'
            self.handle_static()
        else:
            self.content_type = 'image/jpeg'
            self.handle_image()

    def handle_static(self):
        ''''处理js、css文件'''
        static_file = setting.BASE_PATH
        file_path_li = self.path.split("/")
        for i in file_path_li:
            static_file = os.path.join(static_file, i)
        try:
            with open(static_file, 'r', encoding='UTF-8') as f:
                text = f.read()
        except FileNotFoundError as err:
            print(f"{static_file}不存在！")
            self.code = '404 not found'
        else:
            self.content = text

    def handle_image(self):
        '''处理图片文件'''
        image = setting.BASE_PATH
        path_li = self.path.split('/')
        for i in path_li:
            image = os.path.join(image, i)
        try:
            with open(image, 'rb') as f:
                content_byte = f.read()
        except FileNotFoundError as err:
            print(f"{image}文件不存在")
            self.code = '404 not found'
        else:
            self.content = content_byte

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"没有属性{key}")

    def __setattr__(self, key, value):
        # 不可写成self.key=value,会造成无穷递归
        self[key] = value
