# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import ImageCreateView, ImageDetailView, ImageDetailViewB, image_like, ImageListView

urlpatterns = [
    url(r'^create/$', ImageCreateView.as_view(), name='create'),
    url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', ImageDetailView.as_view(), name='detail'),
    url(r'^detail/(?P<id>\d+)/$', ImageDetailViewB.as_view(), name='detail2'),
    url(r'^like/$', image_like, name='like'),
    url(r'^$', ImageListView.as_view(), name='list')
]