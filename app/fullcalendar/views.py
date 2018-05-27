from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.serializers import serialize
from userauth.models import CustomUser
from django.contrib.auth.decorators import login_required

from .models import Event, Department
from django.contrib.auth import get_user_model


@login_required
def fullcalendar(request):
    """ index för kalender applikationen """
    return render(request, 'fullcalendar/calendar.html')


@login_required
def events(request):
    """ Hämtar alla event från databasen i JSON format """
    return JsonResponse(list(Event.objects.all().values()), safe=False)


@login_required
def upd_event(request):
    """ Uppdaterar ägande på ett pass = bokning """
    event_id = request.POST.get("event_id")
    username = request.user.pk
    print ("\nEvent_id:", event_id, "\nCurrentUser: ", username, "\n--------\n")
    available = Event.objects.filter(pk=event_id, username_id=None).values().exists()

    # Låter enbart användaren boka passet om det är ledigt
    if available == False:
        # Borde vara $if not available:
        raise Exception("Passet är upptaget!")
    elif available == True:
        # Borde vara $if available:
        print(" Passet är ledigt")
        Event.objects.filter(pk=event_id).update(username_id=username)
        return JsonResponse(list(Event.objects.all().values()), safe=False)


@ensure_csrf_cookie
def new_event(request):
    """ Skapar nytt pass """
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
        "dept": dept})


@login_required
def dashboard(request):
    """ Hämtar dashboard och populerar med data. """
    my_events = list(Event.objects.filter(username=request.user.pk).values())
    available_events = list(Event.objects.filter(username=None).values())
    return render(request, 'dashboard.html', {"my_events": my_events, "available_events": available_events})

s
@login_required
def profil(request):
    """ Hämtar profil och populerar med data. """
    user_info = CustomUser.objects.all().filter(id=request.user.pk).values()
    return render(request, 'profile.html', {"user_info": user_info})


def edit_profile(request):
    """ Låter användaren uppdatera sin profil """
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)
