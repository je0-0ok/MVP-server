
from django.urls import path

from . import views
from .views import *

app_name = 'boardapp'

urlpatterns = [
    path('test3/', postaddview, name='test3'),
    path('<int:pk>/delete/', postdelete, name='postdelete'),
    path('<int:pk>/edit/', edit, name='edit'),
]
