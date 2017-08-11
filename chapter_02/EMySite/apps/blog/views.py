# -*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView
from django.core.mail import send_mail
from django.db.models import Count

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag

from .models import Post, Comment
from .forms import EmailPostForm, CommentForm

# Create your views here.


def post_list(request, tag_slug=None):
    """
    这个是我们的文章列表页
    chapter 01,post_list只有一个参数
    chapter 02,增加了tag_slug这个参数
    """
    all_posts = Post.published.all()
    tag = None
    # 查看是否传递了tag_slug标签过来
    if tag_slug:
        print(tag_slug)
        tag = get_object_or_404(Tag, slug=tag_slug)
        all_posts = all_posts.filter(tags__in=[tag])



    # 实现页面分页的选择

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    # Provide Paginator with the request object for complete querystring generation

    paginator = Paginator(all_posts, 2, request=request)  # 获取一共有多少分页

    all_post_page = paginator.page(page)  # 拿到指定的分页的数据

    # print(repr(all_post_page))
    for post in all_post_page.object_list:
        for tag in post.tags.all():
            print(tag.slug)

    return render(request, 'blog/post/list.html', {'page': page,
                                                   'all_post_pages': all_post_page,
                                                   'tag': tag})


def post_detail(request, year, month, day, post):
    """
    文章详情页
    :param request: 
    :return: 
    """
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    # 列出所有的状态为active的评论,这里是使用了 related_name,如果没定义related_name可以使用
    # comment_set，一样的效果
    all_comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        # 用户提交一个post
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # 使用ModelForm的save方法，获取一个Model的实例 new_comment
            new_comment = comment_form.save(commit=False)
            # assign the current post to the comment, 指定当前的文章到评论中
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    return render(request, 'blog/post/detail.html', {'post': post,
                                                     'all_comments': all_comments,
                                                     'comment_form': comment_form,
                                                     'new_comment': new_comment,
                                                     'similar_posts': similar_posts})


class PostListView(View):
    """
    第2种方法:使用类来代替使用函数
    """
    def get(self, request):
        all_posts = Post.objects.all()

        # 实现分页的操作
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        paginator = Paginator(all_posts, 2, request=request)  # 获取一共有多少分页

        all_post_page = paginator.page(page)  # 拿到指定的分页

        return render(request, 'blog/post/list.html', {'all_post_pages': all_post_page})


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    send_flag = False
    if request.method == "POST":
        # Form was submitted,表单被提交上去了
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # From fields passed validation
            cd = form.cleaned_data
            # ....send mail
            post_url = request.build_absolute_uri(post.get_absolute_url()) # 获取当前帖子的完整url

            subject = '{}({}) recommends you reading "{}" '.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {} \n\n {} \'s comments:{}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'luojingen@aliyun.com', [cd['to']])
            send_flag = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {
        'post': post,
        'form': form,
        'send_flag': send_flag})
