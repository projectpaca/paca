from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def news(request):
	''' '''
	news = News.objects.all()
	return render(request, 'news/news_list.html', {"news":news})

def news_detail(request, slug):
	''' '''
	news = News.objects.get(slug=slug)
	return render(request, 'news/news_detail.html', {"news":news})
