# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_auto_20170901_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='时间')),
                ('user_form', models.ForeignKey(related_name='rel_from_set', to=settings.AUTH_USER_MODEL, verbose_name='关注者')),
                ('user_to', models.ForeignKey(related_name='rel_to_set', to=settings.AUTH_USER_MODEL, verbose_name='被关注者')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': '粉丝',
                'verbose_name_plural': '粉丝',
            },
        ),
    ]
