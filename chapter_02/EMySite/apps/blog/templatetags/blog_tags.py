# -*- coding:utf-8 -*-
# 引入系统级库

# 引入django的库
from django import template
# 引入自己的代码库
from ..models import Post


register = template.Library()


@register.simple_tag
def total_post():
    """
    定义一个装饰器，这是一个简单标签
    :return: 
    """
    return Post.published.count()

