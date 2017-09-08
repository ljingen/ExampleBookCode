# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='user_form',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='rel_from_set', verbose_name='关注'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user_to',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='rel_to_set', verbose_name='被关注'),
        ),
    ]
