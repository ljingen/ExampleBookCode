# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='标题', max_length=200)),
                ('slug', models.SlugField(verbose_name='slug', blank=True, max_length=200)),
                ('url', models.URLField(verbose_name='链接')),
                ('image', models.ImageField(verbose_name='图片', upload_to='images/%y/%m/%d', max_length=200)),
                ('description', models.TextField(verbose_name='描述', blank=True)),
                ('created', models.DateField(verbose_name='添加时间', auto_now_add=True, db_index=True)),
                ('user', models.ForeignKey(verbose_name='作者', related_name='images_created', to=settings.AUTH_USER_MODEL)),
                ('user_like', models.ManyToManyField(verbose_name='喜欢', related_name='images_liked', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'verbose_name': '图片信息',
                'verbose_name_plural': '图片信息',
            },
        ),
    ]
