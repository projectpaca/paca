"""
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

class fullcalender(generic.CreateView):
    success_url = reverse_lazy('login')
    template_name = 'fullcalender.html'
"""

from django.http import HttpResponse

class fullcalender (request):
    return HttpResponse("Hello, world. This is the FULLCALENDAR!")

