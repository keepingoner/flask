# -*- coding: utf-8 -*-

# @Time    : 2019-05-31 14:59
# @Author  : jian
# @File    : celeryconfig.py
from datetime import timedelta

CELERYBEAT_SCHEDULE = {

    'add': {
        'task': 'projb.tasks.add',
        'schedule': timedelta(seconds=10),
        'args': (16, 16)
    }

}
