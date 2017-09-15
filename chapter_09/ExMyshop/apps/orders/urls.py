# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from .views import CreateOrderView

urlpatterns = [
    url(r'^create/$', CreateOrderView.as_view(), name='order_create'),
]