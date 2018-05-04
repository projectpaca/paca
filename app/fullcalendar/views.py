from django.shortcuts import get_object_or_404, render
from .models import Event
# from django.db import connection
from django.http import JsonResponse


def fullcalendar (request):
    return render(request, 'fullcalendar/calendar.html')


def events(request):
    """ Hämtar alla event från databasen """
    return JsonResponse(list(Event.objects.all().values()),safe=False)


def new(title, start, end):
    """ Skapar ny bokning """
    new_event = new(title="title", start="start", end="end")
    new_event.save()
    return {"start": start, "end": end, "title": title}


def detail(request, shift_id):
    # Inte fått denna att funka
    """ Denna funktion ska visa detaljer om ett specifikt pass """
    event = get_object_or_404(Event, pk=event_id)
    return render (request, 'fullcalendar/shift.html')
