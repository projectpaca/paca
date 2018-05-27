from django.urls import path
from django.views.generic import TemplateView
from . import views, models

app_name = 'news'

# Local routing settings 
urlpatterns = [
    path('', views.news, name="list"),
    path('<slug>/', views.news_detail, name="detail"),
]
