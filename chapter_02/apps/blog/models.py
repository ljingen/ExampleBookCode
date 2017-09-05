# -*- coding:utf-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager
# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    """
    文章
    """
    objects = models.Manager()  # The defautl manager. 系统默认的管理器
    published = PublishedManager()  # Our custom manager 我们自定义的管理器
    STATUS_CHOICES = (
        ('draft', u'草稿'),
        ('published', u'发布'),
    )
    title = models.CharField(max_length=200, verbose_name=u'标题')
    author = models.ForeignKey(User, related_name='blog_posts', verbose_name=u'作者')
    slug = models.SlugField(max_length=200, unique_for_date='publish', verbose_name='slug')
    body = models.TextField(verbose_name=u'正文')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    updated = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')
    status = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=10, verbose_name=u'状态')
    # 第三方的taggit管理器
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)
        verbose_name = u'文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        获取Post对象的url地址，利用reverse的反调功能
        :return: 
        """
        print(self.publish.year)
        return reverse('blog:post_detail', args=[self.publish.year,
                                                 self.publish.strftime('%m'),
                                                 self.publish.strftime('%d'),
                                                 self.slug])


class Comment(models.Model):
    """
    评论字段
    """
    post = models.ForeignKey(Post, related_name='comments', verbose_name=u'所属文章')
    name = models.CharField(max_length=50, verbose_name=u'名称')
    email = models.EmailField(verbose_name=u'邮箱')
    body = models.TextField(verbose_name=u'正文')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')
    updated = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    active = models.BooleanField(default=True, verbose_name=u'状态')

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
