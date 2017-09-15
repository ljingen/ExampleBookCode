# -*- coding: utf-8 -*-
from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    """
    需要用户填写的订单表,用于创建新的order对象的表单
    """
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']
