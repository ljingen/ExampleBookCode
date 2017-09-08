# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class Action(models.Model):
    """
    用户活动表
    """
    user = models.ForeignKey(User, related_name='actions', db_index=True)  # 执行操作的用户
    verb = models.CharField(max_length=255)  # 用户执行操作的动作描述

    target_ct = models.ForeignKey(ContentType,
                                  blank=True,
                                  null=True,
                                  verbose_name=u'目标对象',
                                  related_name='target_obj')
    target_id = models.PositiveIntegerField(null=True,
                                            blank=True,
                                            db_index=True,
                                            verbose_name=u'目标id')
    target = GenericForeignKey('target_ct', 'target_id')
    created = models.DateTimeField(auto_now_add=True, db_index=True)  # 创建动作时间

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ('-created',)
        verbose_name = u'活动'
        verbose_name_plural = verbose_name
