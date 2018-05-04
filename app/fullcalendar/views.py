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



    #title = request.get("title")
    #start = request.get("start")
    #end = request.get("end")

    #cursor.execute("INSERT into events (title, start, end) VALUES ('{}', '{}', '{}')".format(title, start, end))
    #return json.dumps(events)

# PACA2
    """jobForm = JobForm(request.POST or None)
    if request.method == 'POST':
        if jobForm.is_valid():
            jobFo = jobForm.save()
            new_job.manager.add(manager)
            new_job.save()"""
#### ANTON
    #'''Create a calendar event'''
    #db = pymysql.connect(DB_HOST,DB_USERNAME, DB_PASSWORD, DB_NAME, cursorclass=pymysql.cursors.DictCursor)
    #cursor = db.cursor()
    #cursor.execute("INSERT into events (title, start, end) VALUES ('{}', '{}', '{}')".format(title, start, end))
    #db.commit()
    #db.close()
    #return {"start": start, "end": end, "title": title}
###


def detail(request, shift_id):
    # Inte fått denna att funka
    """ Denna funktion ska visa detaljer om ett specifikt pass """
    event = get_object_or_404(Event, pk=event_id)
    return render (request, 'fullcalendar/shift.html')

    #https://docs.djangoproject.com/en/2.0/intro/tutorial03/
    #https://docs.google.com/document/d/1_l-36sKyUWxNda1w3_TgmYIuzPVrlPftkxqQYeC7_6A/edit
    #
