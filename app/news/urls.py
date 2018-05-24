from django.urls import path
#from django.views.generic import TemplateView
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news, name="list"),
    path('<slug>/', views.news_detail, name="detail"),

]
