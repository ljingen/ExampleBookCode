# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import ProductDetail, ProductList

urlpatterns = [
    url(r'^$', ProductList.as_view(), name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', ProductList.as_view(), name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', ProductDetail.as_view(), name='product_detail')
]
