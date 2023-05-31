from django.shortcuts import render,redirect,HttpResponse
from team.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def HomePage(request):
  team = TeamModel.objects.all()
  return render(request,'home/home.html',{'team':team})

def AboutPage(request):
  team = TeamModel.objects.all()
  return render(request,'home/about.html',{'team':team})

def SignUp(request):
  if request.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    pass1 = request.POST.get('password')
    pass2 = request.POST.get('confirm_password')
    form = FormWithCaptcha(request.POST)
    if form.is_valid():
      if pass1 != pass2:
        return HttpResponse("Your password and cornfirm password are not same !!!")
      else:
        my_user = User.objects.create_user(name,email,pass1)
        my_user.save()
        return redirect('login')
    else:
      return HttpResponse('Are you robot ?')
  form = FormWithCaptcha()
  return render(request,'registration/signup.html',{'form':form})

def Login(request):
  if request.method == 'POST':
    name = request.POST.get('in_name')
    password = request.POST.get('in_password')
    user = authenticate(request,username=name,password=password)
    if user is not None:
      login(request,user)
      return redirect('home')
    else:
      return HttpResponse("Username or Password is incorrect !!!")
  return render(request,'registration/login.html')

@login_required(login_url='login')
def Logout(request):
  logout(request)
  return redirect('login')