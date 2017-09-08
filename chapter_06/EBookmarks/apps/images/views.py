# -*- coding:utf-8 -*-
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.generic.base import View
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
#from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from common.decorators import ajax_required

from .forms import ImageCreateForm
from .models import Image
from actions.utils import create_action


# Create your views here.
class ImageCreateView(View):
    """
    View for creating an Image using the JavaScript Bookmarklet.
    """
    #@login_required
    # build form with data provided by the bookmarklet via GET
    def get(self, request):
        if not request.user.is_authenticated():
            return render(request, 'account/login.html',{})
        else:
            form = ImageCreateForm(data=request.GET)
            return render(request, 'image/create.html', {'section': 'images',
                                                         'form': form})

    def post(self, request):
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid 表单数据是有效的
            cd = form.cleaned_data  # 取出表单数据
            new_item = form.save(commit=False)
            # assign current user to the item 绑定当前用户到项目上
            new_item.user = request.user

            new_item.save()
            # 调用create_action()添加一条feeds流到数据库里面
            create_action(request.user, 'bookmarked image', new_item)
            messages.success(request, 'Image added successfully')
            # redirect to new created item detail view 重定向到一个新的创建项目详情页面
            return redirect(new_item.get_absolute_url())

        return render(request, 'image/create.html', {'section': 'images',
                                                            'form': form})


class ImageDetailView(View):
    """
    This is the Image detail 
    """
    def get(self, request, id, slug):
        image = get_object_or_404(Image, id=id, slug=slug)

        images_by_popularity = Image.objects.order_by('-total_likes')

        return render(request, 'image/detail.html', {'section': 'images',
                                                     'image': image,
                                                     'images_by_popularity': images_by_popularity})


class ImageDetailViewB(View):
    """
    This is the Image detail 
    """
    def get(self,request, id):
        image = get_object_or_404(Image, id=id)

        return render(request, 'image/detail.html', {'section': 'images',
                                                    'image': image})


@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id', '')
    action = request.POST.get('action', '')

    if image_id and action:
        try:
            """从数据库获取所有图片"""
            image = Image.objects.get(id=int(image_id))

            if action == 'like':
                image.user_like.add(request.user)
                # 生成一条feeds流消息
                create_action(request.user, 'likes', image)
            else:
                image.user_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'ok'})


class ImageListView(View):
    """
    这个是一个图片列表视图
    """
    def get(self, request):
        all_images = Image.objects.all()

        paginator = Paginator(all_images, 8)  # 获取一共有多少分页

        page = request.GET.get('page', 1)

        # 实现页面分页的选择
        try:
            all_images_page = paginator.page(page)
        except PageNotAnInteger:
            all_images_page = paginator.page(1)
        except EmptyPage:
            if request.is_ajax():
                # if the request is AJAX and the page is out of range return an empty page
                return HttpResponse('')
            # If page is out of range deliver last page of results
            all_images_page = paginator.page(paginator.num_pages)  # 拿到指定的分页的数据

        if request.is_ajax():
            return render(request, 'image/list_ajax.html', {'section': 'images',
                                                            'all_images_page': all_images_page})

        return render(request, 'image/image_list.html', {'section': 'images',
                                                         'all_images_page': all_images_page})

    def post(self, request):
        return render(request, 'image/image_list.html', {'section':'images'})
