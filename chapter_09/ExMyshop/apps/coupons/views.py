# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.utils.translation import gettext as _

from .models import Coupon
from .forms import CouponApplyForm


# Create your views here.
class ApplyCouponView(View):
    def get(self, request):
        pass

    def post(self, request):
        now = timezone.now()
        _form = CouponApplyForm(request.POST)
        if _form.is_valid():
            code = _form.cleaned_data['code']
            try:
                coupon = Coupon.objects.get(code__iexact=code,
                                            valid_from__lte=now,
                                            valid_to__gte=now,
                                            active=True)
                request.session['coupon_id'] = coupon.id
            except Coupon.DoesNotExist:
                request.session['coupon_id'] = None
        return redirect('cart:cart_detail')
