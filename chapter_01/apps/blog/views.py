# -*- conding:utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.generic import View,ListView,DetailView

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Post

# Create your views here.


def post_list(request):
    """
    这个是我们的文章列表页
    """
    all_posts = Post.objects.all()

    # 实现页面分页的选择
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    # Provide Paginator with the request object for complete querystring generation

    paginator = Paginator(all_posts, 1, request=request) # 获取一共有多少分页

    all_post_page = paginator.page(page)  # 拿到指定的分页

    return render(request, 'blog/post/list.html', {'all_post_pages': all_post_page})


def post_detail(request, year, month, day, post):
    """
    文章详情页
    :param request: 
    :return: 
    """
    if request.method == 'GET':
        print(u'哈哈,我是一个GET请求')
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request,
                  'blog/post/detail.html',
                  {'post': post})


class PostView(View):
    """
    第2种方法:使用类来代替使用函数
    """
    def get(self,request):
        all_posts = Post.objects.all()

        # 实现分页的操作
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        paginator = Paginator(all_posts, 1, request=request)  # 获取一共有多少分页

        all_post_page = paginator.page(page)  # 拿到指定的分页

        return render(request, 'blog/post/list.html', {'all_post_pages': all_post_page})
