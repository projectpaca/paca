"""
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

class fullcalendar(generic.CreateView):
    success_url = reverse_lazy('login')
    template_name = 'fullcalendar.html'
"""

#from django.http import HttpResponse
from django.shortcuts import render

def fullcalendar (request):
    return render(request, 'fullcalendar/calendar.html')


def new_shift(request):
    if request.method == 'GET':
        event_id = request.GET['event_id'] #NOTERA namn på event_id
    
    return render(request, .8000/calendar/new)
