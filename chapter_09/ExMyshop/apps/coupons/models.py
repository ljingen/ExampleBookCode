# -*- coding:utf-8 -*-

from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator


# Create your models here.
class Coupon(models.Model):
    """
    优惠券数据表
    """
    #  The code that users have to enter in order to apply the coupon to their purchase
    code = models.CharField(max_length=50, unique=True)
    # The datetime value that indicates when the coupon becomes valid.
    valid_from = models.DateTimeField()
    # The datetime value that indicates when the coupon becomes invalid
    valid_to = models.DateTimeField()
    # The discount rate to apply (this is a percentage, so it takes values from 0 to 100)
    discount = models.IntegerField(validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])
    # A boolean that indicates whether the coupon is active
    active = models.BooleanField()

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = u'优惠券'
        verbose_name_plural = verbose_name
