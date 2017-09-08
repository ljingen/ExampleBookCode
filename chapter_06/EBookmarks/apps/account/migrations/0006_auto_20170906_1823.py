# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20170906_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='user_form',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='关注', related_name='rel_from_set'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user_to',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='被关注', related_name='rel_to_set'),
        ),
    ]
