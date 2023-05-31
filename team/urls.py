from django.urls import path
from .views import *

urlpatterns = [
    path('team/',TeamView,name='team'),
    path('news/',NewsView,name='news'),
    path('newsinfo/<str:title>/',InfoNewsView,name='newsinfo')
]