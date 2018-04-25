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
