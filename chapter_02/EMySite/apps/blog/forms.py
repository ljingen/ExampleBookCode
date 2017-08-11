# -*- coding: utf-8 -*-
from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    """
    这个邮件的发送表格，发送会有异常
    """
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
