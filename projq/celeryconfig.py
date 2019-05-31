# -*- coding: utf-8 -*-

# @Time    : 2019-05-31 14:56
# @Author  : jian
# @File    : celeryconfig.py

from kombu import Queue

CELERY_QUEUES = (  # 定义任务队列

    Queue('default', routing_key='task.#'),  # 路由键以“task.”开头的消息都进default队列

    Queue('web_tasks', routing_key='web.#'),  # 路由键以“web.”开头的消息都进web_tasks队列

)

CELERY_DEFAULT_EXCHANGE = 'tasks'  # 默认的交换机名字为tasks
CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'  # 默认的交换类型是topic
CELERY_DEFAULT_ROUTING_KEY = 'task.default'  # 默认的路由键是task.default，这个路由键符合上面的default队列

CELERY_ROUTES = {

    'projq.tasks.add': {  # tasks.add的消息会进入web_tasks队列

        'queue': 'web_tasks',

        'routing_key': 'web.add',

    }

}
