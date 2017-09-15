# -*- coding: utf-8 -*-
import datetime

from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from .models import Action


def create_action(user, verb, target=None):
    """
    一个用户给某张图片打上书签
    一个用户喜欢或不喜欢某张图片
    一个用户创建一个账户
    一个用户关注或不关注某个用户
    上述事物都会调用该方法来创建一条feed流
    """
    now = timezone.now()  # 获得当前的时间
    last = datetime.timedelta(seconds=60)  # 在当前时间上减少1分钟
    last_minute = now - last  # 最后一次时间，在当前时间减少一分钟是最后一次时间

    print(now, last, last_minute)
    similar_actions = Action.objects.filter(user_id=user.id,
                                            verb=verb,
                                            created__gte=last_minute)  # 取出所有创建时间 >= 最后时间的数据(1分钟前)
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(target_ct=target_ct,
                                                 target_id=target.id)

    # 如果创建时间>= 最后时间 的数据为空，那就直接保存
    if not similar_actions:
        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True
    return False
