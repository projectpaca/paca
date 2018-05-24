from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.serializers import serialize
from userauth.models import CustomUser
from django.contrib.auth.decorators import login_required

from .models import Event, Department
from django.contrib.auth import get_user_model

@login_required
def fullcalendar (request):
    return render(request, 'fullcalendar/calendar.html')

@login_required
def events(request):
    """ Hämtar alla event från databasen """
    return JsonResponse(list(Event.objects.all().values()),safe=False)


@login_required
def upd_event(request):
    """ Uppdaterar bokning """
    event_id = request.POST.get("event_id")
    username = request.user.pk
    print ("\nEvent_id:", event_id, "\nCurrentUser: ", username, "\n--------\n")
    available = Event.objects.filter(pk=event_id, username_id=None).values().exists()
    if available == False:
        # print("Passet är upptaget!")
        #return JsonResponse(list(Event.objects.all().values()),safe=False)
        raise Exception("Passet är upptaget!")
        # return render(request, 'fullcalendar/calendar.html')
    elif available == True:
        print(" Passet är ledigt")
        Event.objects.filter(pk=event_id).update(username_id=username)
        return JsonResponse(list(Event.objects.all().values()),safe=False)
        return render(request, 'fullcalendar/calendar.html')

    # ledig_test = Event.objects.filter(pk=event_id).values().exists(username_id=None)
    # print(type(ledig_test))
    # print(ledig_test)

    """
    Hämta username as bokad_på på pass där pk = Event_id
    IF bokad_på != "":
        return "Pass upptaget!"
    ELSE (bokad_på == ""):
        event.objects.update pass.... (Event.objects.filter(pk=event_id).update(username=username))
    fullcal(request)
    """

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
        "dept": dept })

@login_required
def dashboard(request):
    my_events = list(Event.objects.filter(username=request.user.pk).values())
    available_events = list(Event.objects.filter(username=None).values())
    return render (request, 'dashboard.html',{"my_events": my_events, "available_events": available_events})

@login_required
def profil(request):
    user_info = CustomUser.objects.all().filter(id=request.user.pk).values()
    return render(request, 'profile.html', {"user_info": user_info})


# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=request.CustomUser)
#         if form.is_valid():
#             form.save()
#             message = "Dina ändringar har nu sparats!"
#             return render(request, 'edit_profile.html', {'message':message, 'form':form})
#         else:
#             message=None
#     form = EditProfileForm(request.POST or None, instance=request.CustomUser)
#     args = {'form': form}
#     return render(request, 'edit_profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)

