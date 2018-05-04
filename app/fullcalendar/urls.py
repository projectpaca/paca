from django.urls import path
from django.views.generic import TemplateView
from . import views
<<<<<<< HEAD
=======
from .views import NewShift
>>>>>>> userauth2

# app_name = 'fullcalendar'
# Detta är namespacing!

urlpatterns = [
    # Allt här ligger efter /calendar
    path( r'', views.fullcalendar, name='fullcalendar'),

<<<<<<< HEAD
    #Hämtar alla events i JSON format
    path(r'events', views.events),

    # Sparar ett nytt event till databasen
    path( r'new', views.new),
        #NewShift.as_view()),

=======
    #path( r'new$', NewShift.as_view()),
>>>>>>> userauth2
    #path( r'new', views.new_shift, name='new_shift'),
        # Ska new$ peka på fullcalendar igen
        # eller gör det så att sidan laddas om?
    path(r'<int:shift_id>', views.detail, name='detail'),
]
