# -*- coding:utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.


# settings.AUTH_USER_MODEL
class Image(models.Model):

    objects = models.Manager()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', verbose_name=u'作者')
    title = models.CharField(verbose_name=u'标题', max_length=200)
    slug = models.SlugField(verbose_name=u'slug', max_length=200, blank=True)
    url = models.URLField(verbose_name=u'链接', max_length=200)
    image = models.ImageField(verbose_name=u'图片', upload_to='images/%y/%m/%d', max_length=200)
    description = models.TextField(verbose_name=u'描述', blank=True)
    created = models.DateField(verbose_name=u'添加时间', auto_now_add=True, db_index=True)

    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True,
                                       verbose_name=u'喜欢')

    total_likes = models.PositiveIntegerField(db_index=True, default=0, verbose_name=u'Total Likes')

    class Meta:
        verbose_name = u'图片信息'
        verbose_name_plural = verbose_name

    # 调用实例，返回实例的标题
    def __str__(self):
        return self.title

    # 如果当前实例的slug是空，那么自动生成slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=(self.id, self.slug))