# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import AddToCartView, RemoveFromCartView, CartDetailView


urlpatterns = [
    url(r'^$', CartDetailView.as_view(), name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', AddToCartView.as_view(), name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)$', RemoveFromCartView.as_view(), name='cart_remove'),
]
