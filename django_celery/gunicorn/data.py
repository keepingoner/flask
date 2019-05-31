# -*- coding: utf-8 -*-

# @Time    : 2019-05-31 16:21
# @Author  : jian
# @File    : data.py.py
from django import setup
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')  # 在环境变量中设置配置文件
setup()
from gunicorn.models import TestModel

data_set = {
    'ls': """import os\r\nprint(os.listdir())""",
    'pwd': """import os\r\nprint(os.getcwd())""",
    'hello world': """print('Hello world')"""
}
for name, code in data_set.items():
    TestModel.objects.create(name=name, code=code)

print('Done')
