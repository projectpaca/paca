from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import NewShift

# app_name = 'fullcalendar'
# Detta är namespacing!

urlpatterns = [
    # Allt här ligger efter /calendar
    path( r'', views.fullcalendar, name='fullcalendar'),

    #path( r'new$', NewShift.as_view()),
    #path( r'new', views.new_shift, name='new_shift'),
        # Ska new$ peka på fullcalendar igen
        # eller gör det så att sidan laddas om?
    path(r'<int:shift_id>', views.detail, name='detail'),
]
