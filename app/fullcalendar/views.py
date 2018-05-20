from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.serializers import serialize
from .models import Event


def fullcalendar (request):
    return render(request, 'fullcalendar/calendar.html')


def events(request):
    """ Hämtar alla event från databasen """
    return JsonResponse(list(Event.objects.all().values()),safe=False)


def upd_event(request):
    """ Uppdaterar bokning """
    event_id = request.POST.get("event_id")
    username = request.user.pk
    print ("\nEvent_id:", event_id, "\nCurrentUser: ", username, "\n--------\n")

    Event.objects.filter(pk=event_id).update(username=username)
    fullcalendar(request)


@ensure_csrf_cookie
def new_event(request):
    """ Skapar ny bokning """
    title = request.POST.get("title")
    start = request.POST.get("start")
    end = request.POST.get("end")
    req_usr = request.POST.get("req_usr")
    dept = request.POST.get("dept")

    event = Event(title=title, start=start, end=end, req_usr=req_usr, dept=dept)
    event.save()

    return JsonResponse({
        "title": title,
        "start": start,
        "end": end,
        "req_usr": req_usr,
        "dept": dept

    })



    # return  JsonResponse ({}) ?

'''
    username = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=True,
        verbose_name="Bokad på",
        on_delete=models.CASCADE
    )

    event = Event(title=title, start=start, end=end, req_usr=req_usr, dept=dept)
    event.save()

    return JsonResponse({
        "title": title,
        "start": start,
        "end": end,
        "req_usr": req_usr,
        "dept": dept
    })
'''
