from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views
from .views import *

app_name = 'blogapp'
urlpatterns = [
    #로그인, 로그아웃
    path('signup/', views.signup, name='user_signup'),
    path('test/', test, name='test'),
    path('',index, name='index')
]