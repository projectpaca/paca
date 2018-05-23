from django.shortcuts import render
from .models import News

# Create your views here.

# Kanske att du måste skicka med News som argument
def news(request):
    ''' '''
    return render(request, 'news_list.html')
