import re
from datetime import datetime
from urllib import parse


class Request():
	def __init__(self, environ):
		self._clean_request(environ)
		# self.print_environ(environ)

	def _clean_request(self, environ):
		'''
		构造请求参数，绑定实例对象上
		'''
		self.method = environ.get('REQUEST_METHOD')
		self.path = environ.get('PATH_INFO')
		self.content_type = environ.get('CONTENT_TYPE')
		self.length = environ.get('CONTENT_LENGTH') or 0
		self.GET = Request.parse_di(environ.get('QUERY_STRING'))
		self.POST = Request.parse_di(environ.get('wsgi.input').read(int(self.length)).decode())
		self.POST = {k: Request.url_decode(v) for k, v in self.POST.items()}
		self.cookie = environ.get('HTTP_COOKIE') or ''
		self.user = Request.parse_di(self.cookie)

	@staticmethod
	def parse_di(url):
		'''
		对类似get参数的字符串解析成字典
		'''
		if url:
			li = url.split('&')
			new_li = [[i.split("=")[0], i.split("=")[1]] for i in li]
			return dict(new_li)
		return {}

	@staticmethod
	def url_decode(_s):
		'''urlencode解码'''
		if _s:
			d = "keys=" + _s
			return parse.parse_qs(d)['keys'][0]
		return _s

	def print_environ(self, environ):
		'''
		打印请求的环境变量
		'''
		print("*"*50)
		for k, v in environ.items():
			print(k+":"+str(v))
		print("*"*50)