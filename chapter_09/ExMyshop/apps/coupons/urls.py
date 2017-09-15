# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import ApplyCouponView

urlpatterns = [
    url(r'^apply/$', ApplyCouponView.as_view(), name='apply'),
]