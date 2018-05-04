from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import NewShift

# app_name = 'fullcalendar'
# Detta är namespacing!

urlpatterns = [
    path( r'', views.fullcalendar, name='fullcalendar'),

    # Hämtar alla events i JSON format
    path(r'events', views.events),

    # Sparar ett nytt event till databasen
    path( r'new', views.new),

    # Tänkt att visa info om ett pass
    # path(r'<int:shift_id>', views.detail, name='detail'),
]
