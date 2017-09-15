# -*- coding:utf-8 -*-
from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from shop.models import Product
from coupons.models import Coupon


# Create your models here.
class Order(models.Model):
    """
    订单表，生成一张订单
    """
    first_name = models.CharField(max_length=50, verbose_name=u'名字')
    last_name = models.CharField(max_length=50, verbose_name=u'姓')
    email = models.EmailField(verbose_name=u'邮箱')
    address = models.CharField(max_length=200, verbose_name=u'地址')
    postal_code = models.CharField(max_length=20, verbose_name=u'邮编')
    city = models.CharField(max_length=100, verbose_name=u'城市')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')
    updated = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')
    paid = models.BooleanField(default=False, verbose_name=u'支付状态')

    coupon = models.ForeignKey(Coupon, related_name='orders', null=True, blank=True, verbose_name=u'优惠券')
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0),
                                                          MaxValueValidator(100)], verbose_name=u'折扣率')

    class Meta:
        verbose_name = u'订单表'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost*(self.discount / Decimal('100'))


class OrderItem(models.Model):
    """
    订单中的购物项目
    """
    order = models.ForeignKey(Order, related_name='items', verbose_name=u'订单')
    product = models.ForeignKey(Product,related_name='order_items', verbose_name=u'商品')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'价格')
    quantity = models.PositiveIntegerField(default=1, verbose_name=u'数量')

    class Meta:
        verbose_name = u'购物车物品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        """
        返回一共开销
        """
        return self.price * self.quantity
