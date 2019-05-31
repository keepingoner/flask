# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('code', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('changed_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
