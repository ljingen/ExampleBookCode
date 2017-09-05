# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(verbose_name='标题', max_length=200)),
                ('slug', models.SlugField(unique_for_date='publish', verbose_name='slug', max_length=200)),
                ('body', models.TextField(verbose_name='正文')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('status', models.CharField(choices=[('draft', '草稿'), ('published', '发布')], verbose_name='状态', max_length=10, default='draft')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='作者', related_name='blog_posts')),
            ],
            options={
                'verbose_name_plural': '文章',
                'verbose_name': '文章',
                'ordering': ('-publish',),
            },
        ),
    ]
