# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-08 12:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tagging.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('rank', models.IntegerField(default=0, verbose_name='排序')),
                ('status', models.IntegerField(choices=[(0, '正常'), (1, '草稿'), (2, '删除')], default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('img', models.FileField(upload_to='./upload/img/category/', verbose_name='上传图片')),
                ('child', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='beio_blog.Category', verbose_name='下级分类')),
            ],
            options={
                'ordering': ['rank', '-create_time'],
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('content', models.TextField(default='', verbose_name='正文')),
                ('summary', models.TextField(default='', verbose_name='摘要')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='发布时间')),
                ('viewsum', models.IntegerField(default=0, verbose_name='浏览量')),
                ('commentsnum', models.IntegerField(default=0, verbose_name='评论量')),
                ('likenum', models.IntegerField(default=0, verbose_name='点赞数')),
                ('tags', tagging.fields.TagField(blank=True, help_text='用逗号分隔', max_length=255, verbose_name='标签')),
                ('is_top', models.BooleanField(default=False, verbose_name='置顶')),
                ('rank', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(0, '正常'), (1, '草稿'), (2, '删除')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='beio_blog.Category', verbose_name='分类')),
            ],
        ),
    ]
