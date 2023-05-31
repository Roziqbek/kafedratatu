from django.urls import path
from .views import *

urlpatterns = [
  path('about/',AboutPage,name='about'),
  path('signup/',SignUp,name='signup'),
  path('login/',Login,name='login'),
  path('logout/',Logout,name='logout'),
]