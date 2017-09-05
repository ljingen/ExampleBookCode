# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('body', models.TextField(verbose_name='正文')),
                ('created', models.DateTimeField(verbose_name='添加时间', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='修改时间', auto_now=True)),
                ('active', models.BooleanField(default=True, verbose_name='状态')),
                ('post', models.ForeignKey(related_name='comments', verbose_name='所属文章', to='blog.Post')),
            ],
            options={
                'ordering': ('created',),
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]
