from django.shortcuts import render,HttpResponse,redirect
from .models import *


def ContactView(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    ContactModel.objects.create(name=name,email=email,subject=subject,message=message)
    return redirect('home')
  return render(request,'contact/contact.html')


def TeacherView(request):
  context = TeacherModell.objects.all()
  return render(request,'contact/services.html',{'context':context})


def TeachersInfoView(request,name):
  obj = InfoModell.objects.get(name=name)
  if request.method == 'POST':
    title = request.POST.get('title')
    pdf = request.POST.get('filename')
    types = request.POST.get('types')
    date = request.POST.get('date')
    time = request.POST.get('time')
    doc = DocumentModel.objects.create(title=title,document=pdf,types=types,date=date,time=time)
    doc.save()
    return redirect('teachers')
  return render(request,'contact/info.html',{'obj':obj})
