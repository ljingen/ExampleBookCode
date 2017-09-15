# -*- coding:utf-8 -*-

from django import forms
from django.contrib.auth.models import User

from .models import Profile


class LoginForm(forms.Form):
    """
    定义一个表单，这个表单是为了让用户可以进行登录授权
    username:用户名
    password : 用户密码
    """
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label=u'密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label=u'确认密码', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don\'t match.")
        return cd['password2']


class UserEditForm(forms.ModelForm):
    """
    允许用户编辑它们的 first name,last name, e-mail 这些储存在 User 模型(model)中的内置字段
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    """
    允许用户编辑我们存储在定制的 Profile 模型(model)中的额外数据。用户可以编辑他们的生日数据以及为他们的 
    profile 上传一张照片
    """
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
