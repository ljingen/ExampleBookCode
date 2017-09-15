# -*- coding: utf-8 -*-
from django import forms


class CouponApplyForm(forms.Form):
    """折扣券输入表"""
    code = forms.CharField()