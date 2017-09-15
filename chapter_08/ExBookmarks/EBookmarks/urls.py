"""EBookmarks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.static import serve

from EBookmarks.settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^account/', include('apps.account.urls', namespace='account')),
    url(r'^account/', include('account.urls', namespace='accounts')),
    url(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^images/', include('images.urls',namespace='images')),
    url(r'^actions/', include('actions.urls', namespace='actions')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

