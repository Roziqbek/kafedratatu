from django.urls import path
from .views import *


urlpatterns = [
  path('contact/',ContactView,name='contact'),
  path('teachers/',TeacherView,name='teachers'),
  path('info/<str:name>/',TeachersInfoView,name='info'),
]