from django.shortcuts import render
from .models import News
from django.http import HttpResponse

# Create your views here.

# Kanske att du måste skicka med News som argument
def news(request):
    ''' '''
    news = News.objects.all().order_by('date')
    return render(request, 'news_list.html', {'news':news})

def news_detail(request,slug):
    #return HttpResponse(slug)
    news = News.objects.get(slug=slug)
    return render(request, 'news/news_detail.html', {'news':news})
