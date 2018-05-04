from django.shortcuts import get_object_or_404, render
from .models import Event
from django.db import connection

def fullcalendar (request):
    return render(request, 'fullcalendar/calendar.html')

def events(request):
    """ Hämtar alla event från databasen """
    # connect till databasen
    with connection.cursor() as cursor:
        # Skicka SELECT sats
        cursor.execute("SELECT * FROM Events")
        # Hämta & returnera som JSON
        return json.dumps(cursor.fetchall())

def new(request):
    """if request.method == 'GET':
        event_id = request.GET['event_id'] #NOTERA namn på event_id
        booked_event"""
    title = request.get("title")
    start = request.get("start")
    end = request.get("end")

    events = calendar.new(title, start, end)
    return json.dumps(events)
    #return render(request, .8000/calendar/new)'''

def detail(request, shift_id):
    # Inte fått denna att funka
    """ Denna funktion ska visa detaljer om ett specifikt pass """
    event = get_object_or_404(Event, pk=event_id)
    return render (request, 'fullcalendar/shift.html')

    #https://docs.djangoproject.com/en/2.0/intro/tutorial03/
    #https://docs.google.com/document/d/1_l-36sKyUWxNda1w3_TgmYIuzPVrlPftkxqQYeC7_6A/edit
    #
