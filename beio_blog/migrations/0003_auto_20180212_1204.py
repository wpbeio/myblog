# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-12 04:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beio_blog', '0002_auto_20180211_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.CharField(default='', max_length=200, verbose_name='摘要'),
        ),
    ]
