# -*- coding: utf-8 -*-

# @Time    : 2019-05-31 8:57
# @Author  : jian
# @File    : celery.py
from __future__ import absolute_import
from celery import Celery

app = Celery('proj', include=['proj.tasks'])

app.config_from_object('proj.celeryconfig')

if __name__ == '__main__':
    app.start()
