from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.fullcalendar, name='fullcalendar'),
    path('events', views.events),
    path('new', views.new_event),
    path('upd_event', views.upd_event),
    path('dash', views.dashboard, name='index'),
    path('profile/', views.profil),
    path('profile/edit', views.edit_profile)
]
