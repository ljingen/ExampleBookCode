# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import LoginView, dashboard, RegisterView, UserProfileEditView, UseListView, UseDetailView, user_follow

urlpatterns = [
    # The user login views
    # url(r'^login/$', LoginView.as_view(), name='login'),  # 用户登录
    # 用户登录 user login
    url(r'^$', dashboard,name='dashboard'),
    url(r'login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^logout-then-login', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    # 修改密码 change password
    url(r'^password-change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^password-change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    # 重置密码 reset password
    url(r'^password-reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password-reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'password-reset/complete/$', 'django.contrib.auth.views.password_reset_complete',
        name='password_reset_complete'),
    # 用户注册 user register
    url(r'register/$', RegisterView.as_view(), name='register'),
    # 修改用户信息 user edit profile
    url(r'edit/$', UserProfileEditView.as_view(), name='edit'),
    # url(r'edit/$', edit, name='edit'),
    # 用户进行关注/取消关注  user follow user ,这个最好放到 user_detail的签名 因为他和user_detail一样
    url(r'user/follow/$', user_follow, name='user_follow'),
    # 查看用户列表和属性 userlist userprofile
    url(r'^user/$', UseListView.as_view(), name='user_list'),
    url(r'^user/(?P<username>[-\w]+)/$', UseDetailView.as_view(), name='user_detail'),
]
