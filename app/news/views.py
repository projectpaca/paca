from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def news(request):
    '''Gets all news articles from the database and
    returns them in the news_list template.'''
    news = News.objects.all().order_by('-date')
    return render(request, 'news_list.html', {'news': news})


def news_detail(request, slug):
    '''Gets the news article whose slug matches
    the one included in the request, and returns
    it in the news_detail template.'''
    news = News.objects.get(slug=slug)
    return render(request, 'news/news_detail.html', {'news': news})
