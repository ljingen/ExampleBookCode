# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_image_total_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='total_like',
            new_name='total_likes',
        ),
    ]
