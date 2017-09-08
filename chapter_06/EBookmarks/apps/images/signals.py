# -*- coding: utf-8 -*-
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Image


@receiver(m2m_changed, sender=Image.user_like.through)
def users_like_changed(sender, instance, **kwargs):
    """
    这是一个接收器,是一个接收函数，一个信号源，会有无数个接受函数用来监听信号
    要接收信号，需要注册一个 receiver 函数。这个函数在信号被发送时调用。信号是通过Signal.connect()
    方法发送的
    Signal.connect(receiver[,sender=None, week=True,dispatch_uid=None)])
    参数:receiver ----接收函数
        weak ---默认django把信号处理器视作弱作用，若你的receiver是局部函数会被垃圾回收，为防止发生，东connect()
        调用时传入weak=True
    :param sender:  唯一的信号发送方，保证这个接收器只处理 右 Image.user_like触发的signals.
    :param instance: 实例
    :param kwargs: 最前面的代表这个信号源，右sender发送的什么类型的信号会被这个接收器出来
    :return: 
    """
    instance.total_likes = instance.user_like.all().count()
    instance.save()

