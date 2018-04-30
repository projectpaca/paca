from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # Allt här ligger efter /calendar
    path( r'', views.fullcalendar, name='fullcalendar'),
    path( r'new$', views.new_shift(), name='fullcalendar'),
        # Ska new$ peka på fullcalendar igen
        # eller gör det så att sidan laddas om?
]
