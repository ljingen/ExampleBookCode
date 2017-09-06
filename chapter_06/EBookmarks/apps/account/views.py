# -*- coding:utf-8 -*-

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.generic.base import View

from common.decorators import ajax_required
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile, Contact
from images.models import Image

# Create your views here.


class LoginView(View):
    """
    用户登录视图
    """
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'account/login.html', {'form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')

            user = authenticate(username=user_name, password=pass_word)  # 根据传递的用户名密码判断用户是否存在，如果存在返回一个User

            if user is not None:
                if user.is_active:
                    login(request, user)  # 将用户登录信息放到session里面
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disable account')
            else:
                return HttpResponse('Invalid login')
        else:
            return render(request, 'account/login.html', {'form': login_form})


@login_required
def dashboard(request):
    '''
    section: 在返回字段里面，告诉前端，当前所在的页面
    :param request: 
    :return: 
    '''
    # count = request.user.images_created.count
    count = Image.objects.filter(user=request.user).count()

    return render(request, 'account/dashboard.html', {'section': 'dashboard',
                                                      'count': count})


class RegisterView(View):
    """
    用户注册视图，处理用户注册，如果请求页面返回一个注册页面， 如果是提交表单
    则进行注册处理
    """
    def get(self, request):
        user_form = UserRegistrationForm()
        return render(request, 'account/register.html', {'user_form': user_form})

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # create a new user object but avoid savint it yet
            new_user = user_form.save(commit=False)
            # set the chose password
            new_user.set_password(user_form.cleaned_data['password'])
            # save the User object
            new_user.save()
            # create the user profile 添加用户属性
            profile = Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
        else:
            return render(request, 'account/register.html', {'user_form': user_form})


class UserProfileEditView(View):
    """
    修改用户的属性视图,修改用户属性,可以编辑用户的资料，根据UserEditForm、ProfileEditForm的字段进行编辑
    """
    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

        return render(request, 'account/edit.html', {'user_form': user_form,
                                                     'profile_form': profile_form})

    def post(self, request):
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save(commit=True)
            messages.success(request, 'Profile updated successfully')
        else:
            # 这个是一个全局
            messages.error(request, 'Error updating your prfile')

        return render(request, 'account/edit.html', {'user_form': user_form,
                                                     'profile_form': profile_form})
# @login_required
# def edit(request):
#     if request.method == 'POST':
#         user_form = UserEditForm(instance=request.user,data=request.POST)
#         profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#     else:
#         user_form = UserEditForm(instance=request.user)
#         profile_form = ProfileEditForm(instance=request.user.profile)
#     return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})


class UseListView(View):
    """
    获取所有的用户列表
    """
    def get(self, request):
        all_users = User.objects.filter(is_active=True)
        return render(request, 'user/list.html', {'section': 'people',
                                                  'all_users': all_users})


class UseDetailView(View):
    """
    用户个人资料页
    """
    def get(self, request, username):
        user = get_object_or_404(User, username=username, is_active=True)
        count = user.followers.all().count()
        print(count)
        return render(request, 'user/detail.html', {'section': 'people',
                                                    'user': user,
                                                    'count': count})


# class UserFollowView(View):
#     """
#     用户关注视图，用户关注/取消关注。
#     只有post数据
#     通过ajax进行提交
#     登录用户才可提交
#     """
#     def get(self):
#         pass
#
#     def post(self, request):
#         user_id = request.POST.get('id')
#         action = request.POST.get('action')
#
#         if user_id and action:
#             try:
#                 user = User.objects.get(id=user_id)
#                 if action == 'follow':
#                     Contact.objects.get_or_create(user_from=request.user,
#                                                   user_to=user)
#                 else:
#                     Contact.objects.filter(user_from=request.user,
#                                            user_to=user).delete()
#                 return JsonResponse({'status': 'ok'})
#             except User.DoesNotExist:
#                 return JsonResponse({'status': 'ko'})
#         return JsonResponse({'status': 'ko'})

@ajax_required
@require_POST
@login_required
def user_follow(request):
   user_id = request.POST.get('id')  # 将被关注的用户
   action = request.POST.get('action')  # 用户关注的动作，有 follow和unfollow

   """
    Contact  {user_from(User类型): 关注人   user_to（User类型）:被关注人，create:创建时间}
   """
   if user_id and action:
       login_user = request.user
       try:
           user = User.objects.get(id=user_id)
           if action == 'follow':
               Contact.objects.create(user_from=login_user, user_to=user)
           else:
               Contact.objects.filter(user_from=login_user,
                                      user_to=user).delete()
           return JsonResponse({'status': 'ok'})
       except User.DoesNotExist:
           return JsonResponse({'status': 'ko'})
   return JsonResponse({'status': 'ko'})