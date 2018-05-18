from django.urls import path
from django.views.generic import TemplateView
from . import views


# app_name = 'fullcalendar'
urlpatterns = [
    path( r'', views.fullcalendar, name='fullcalendar'),
    # Hämtar alla events i JSON format
    path(r'events', views.events),
    # Sparar ett nytt event till databasen
    path( r'new', views.new_event),
    path( r'upd_event', views.upd_event),
]
