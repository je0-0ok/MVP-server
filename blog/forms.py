from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm

from .models import *


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text']


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
