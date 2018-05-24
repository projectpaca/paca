from django.urls import path
from . import views, models

app_name = 'news'

urlpatterns = [
    path('', views.news, name="news"),
    path('<slug>/', views.news_detail, name="news_detail"),

]
