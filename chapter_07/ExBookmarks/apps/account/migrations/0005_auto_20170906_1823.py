# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20170906_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='user_form',
            field=models.ForeignKey(related_name='rel_from_set', to='account.Profile', verbose_name='关注'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user_to',
            field=models.ForeignKey(related_name='rel_to_set', to='account.Profile', verbose_name='被关注'),
        ),
    ]
