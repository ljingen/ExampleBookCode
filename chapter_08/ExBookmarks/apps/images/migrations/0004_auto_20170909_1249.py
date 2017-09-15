# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_auto_20170908_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='total_likes',
            field=models.PositiveIntegerField(verbose_name='Total Likes', db_index=True, default=0),
        ),
    ]
