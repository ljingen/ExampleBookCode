# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0002_auto_20170912_1724'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(verbose_name='优惠券', related_name='orders', default=2, to='coupons.Coupon'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], default=0, verbose_name='折扣率'),
        ),
    ]
