"""
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

class fullcalendar(generic.CreateView):
    success_url = reverse_lazy('login')
    template_name = 'fullcalendar.html'
"""

from django.shortcuts import get_object_or_404, render
from .models import Event

def fullcalendar (request):
    return render(request, 'fullcalendar/calendar.html')


class NewShift():
    def new(request):
        """if request.method == 'GET':
            event_id = request.GET['event_id'] #NOTERA namn på event_id
            booked_event"""
        return render(request, 'fullcalendar/calendar.html')
        #return render(request, .8000/calendar/new)'''

def detail(request, shift_id):
    # Inte fått denna att funka
    """ Denna funktion ska visa detaljer om ett specifikt pass """
    event = get_object_or_404(Event, pk=event_id)
    return render (request, 'fullcalendar/shift.html')

    #https://docs.djangoproject.com/en/2.0/intro/tutorial03/
    #https://docs.google.com/document/d/1_l-36sKyUWxNda1w3_TgmYIuzPVrlPftkxqQYeC7_6A/edit
    #
