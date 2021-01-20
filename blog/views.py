from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *

def index(request):
    return render(request, 'index.html')

def test(request):
    form_class=PostForm
    return render(request,'test.html',{'form':form_class})

#회원가입
def signup(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            new_user=User.objects.create_user(**form.cleaned_data)
            login(request,new_user)
            return redirect('index.html')
    else:
        form = UserForm
        context={
            'form':form,
        }
        return render(request,'signup.html',context)