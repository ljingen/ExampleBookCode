# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.base import View

from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
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
