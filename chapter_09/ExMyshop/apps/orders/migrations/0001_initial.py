# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='名字')),
                ('last_name', models.CharField(max_length=50, verbose_name='姓')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('address', models.CharField(max_length=200, verbose_name='地址')),
                ('postal_code', models.CharField(max_length=20, verbose_name='邮编')),
                ('city', models.CharField(max_length=100, verbose_name='城市')),
                ('created', models.DateTimeField(verbose_name='添加时间', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('paid', models.BooleanField(default=False, verbose_name='支付状态')),
            ],
            options={
                'verbose_name_plural': '订单表',
                'ordering': ('-created',),
                'verbose_name': '订单表',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='数量')),
                ('order', models.ForeignKey(to='orders.Order', related_name='items', verbose_name='订单')),
                ('product', models.ForeignKey(to='shop.Product', related_name='order_items', verbose_name='商品')),
            ],
            options={
                'verbose_name_plural': '购物车物品',
                'verbose_name': '购物车物品',
            },
        ),
    ]
