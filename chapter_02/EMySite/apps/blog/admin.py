# -*- coding:utf-8 -*-

from django.contrib import admin
from .models import Post, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    """
    Post的管理类
    """
    # list_display 控制那些行会在前端显示
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    # list_filter 控制那些的字段将有过滤,在页面右侧显示过滤器
    list_filter = ('status', 'created', 'publish', 'author')
    # search_fields 列出可以被过滤的字段，在页面顶部显示 搜索
    search_fields = ('title', 'body')
    # prepopulated_fields
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    # there is a bar to navigate quickly through a date hierarchy，有一个可以快速通过日期层次结构导航的栏。
    date_hierarchy = 'publish'
    # 有一个根据status 和 publish 进行排序的功能
    ordering = ['status', 'publish']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Comment,CommentAdmin)
admin.site.register(Post, PostAdmin)
