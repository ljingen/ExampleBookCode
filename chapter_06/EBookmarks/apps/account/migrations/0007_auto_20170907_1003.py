# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20170906_1823'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='user_form',
            new_name='user_from',
        ),
    ]
