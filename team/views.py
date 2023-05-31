from django.shortcuts import render
from .models import *

def TeamView(request):
    team = TeamModel.objects.all()
    return render(request,'team/team.html',{'team':team})

def NewsView(request):
    context = NewsModel.objects.all()
    return render(request,'team/news.html',{'context':context})

def InfoNewsView(request,title):
    new = InfoNewsModel.objects.get(title=title)
    return render(request,'team/info.html',{'new':new})