# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(db_index=True, verbose_name='商品类别', max_length=200)),
                ('slug', models.SlugField(verbose_name='slug', max_length=200)),
                ('created', models.DateTimeField(verbose_name='添加时间', auto_now_add=True)),
            ],
            options={
                'verbose_name': '商品类别',
                'verbose_name_plural': '商品类别',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(db_index=True, verbose_name='商品名称', max_length=200)),
                ('slug', models.SlugField(verbose_name='slug', max_length=200)),
                ('image', models.ImageField(verbose_name='商品图片', blank=True, upload_to='products/%y/%m/%d')),
                ('description', models.TextField(verbose_name='商品描述', blank=True)),
                ('price', models.DecimalField(decimal_places=2, verbose_name='商品单价', max_digits=10)),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='商品库存')),
                ('available', models.BooleanField(default=True, verbose_name='是否可售')),
                ('created', models.DateTimeField(verbose_name='添加时间', auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('category', models.ForeignKey(verbose_name='商品类别', to='shop.Category', related_name='products')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]
