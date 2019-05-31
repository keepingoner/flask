# -*- coding: utf-8 -*-

# @Time    : 2019-05-31 16:22
# @Author  : jian
# @File    : rest_test.py

from django import setup
import os

# 加载配置
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')
setup()

from rest_framework import serializers


class TestSeriOne(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    age = serializers.IntegerField()

frontend_data = {
    'name': 'ucag',
    'age': 18
}

test = TestSeriOne(data=frontend_data)
if test.is_valid():
    print(test.validated_data)
