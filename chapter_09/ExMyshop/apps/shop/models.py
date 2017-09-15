# -*- coding:utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name=u'描述')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'数据')


class Category(models.Model):
    """
    商品类目表
    """
    name = models.CharField(max_length=200, db_index=True, verbose_name=u'商品类别')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name=u'slug')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        ordering = ('-name',)
        verbose_name = u'商品类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    """
    商品表
    """
    category = models.ForeignKey(Category, related_name='products', verbose_name=u'商品类别')
    name = models.CharField(max_length=200, db_index=True, verbose_name=u'商品名称')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name=u'slug')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True, verbose_name=u'商品图片')

    description = models.TextField(blank=True, verbose_name=u'商品描述')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'商品单价')
    stock = models.PositiveIntegerField(verbose_name=u'商品库存', default=0)

    available = models.BooleanField(default=True, verbose_name=u'是否可售')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')
    updated = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')

    class Meta:
        ordering = ('name',)
        verbose_name = u'商品表'
        verbose_name_plural = verbose_name
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
