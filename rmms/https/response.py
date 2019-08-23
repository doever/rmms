import re
import json


class ResponseBase(dict):
    def __init__(self, code=None, content_type=None, content=None, kwargs=None):
        super().__init__()
        self.code = code
        self.content_type = content_type
        self.content = content
        if kwargs and isinstance(kwargs, dict):
            for k, v in kwargs.items():
                self.k = v

    def error_404(self):
        self.code = '404 not found'
        self.content = "<h1>the page you request was stolen by martians...</h1>"

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"没有属性{key}")

    def __setattr__(self, key, value):
        # 不可写成self.key=value,会造成无穷递归
        self[key] = value


class HttpResponse(ResponseBase):
    def __init__(self, content=None, code='200 ok', content_type='text/plain', kwargs=None):
        super().__init__(code, content_type, content, kwargs)


class JsonResponse(ResponseBase):
    def __init__(self, content=None, code='200 ok', content_type='json', kwargs=None):
        assert isinstance(content, dict), "json序列化需要使用dict"
        super().__init__(code, content_type, json.dumps(content), kwargs)

