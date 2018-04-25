from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path( r'', views.fullcalendar, name='fullcalendar'),
]
