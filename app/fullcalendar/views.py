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
    '''Displays the calendar.'''
    return render(request, 'fullcalendar/calendar.html')


@login_required
def events(request):
    '''Gets all events from database in JSON format.'''
    return JsonResponse(list(Event.objects.all().values()), safe=False)


@login_required
def upd_event(request):
    '''Updates the booked user of a shift.'''
    event_id = request.POST.get('event_id')
    username = request.user.pk
    print ('\nEvent_id:', event_id, '\nCurrentUser: ', username, '\n--------\n')
    available = Event.objects.filter(pk=event_id, username_id=None).values().exists()

    # Only free shifts can be booked
    if available == False:
        raise Exception('Passet är upptaget!')
    elif available == True:
        print(' Passet är ledigt')
        Event.objects.filter(pk=event_id).update(username_id=username)
        return JsonResponse(list(Event.objects.all().values()), safe=False)


@ensure_csrf_cookie
def new_event(request):
    '''Creates a new event.'''
    title = request.POST.get('title')
    start = request.POST.get('start')
    end = request.POST.get('end')
    req_usr = request.POST.get('req_usr')
    dept = request.POST.get('dept')
    event = Event(title=title, start=start, end=end, req_usr=req_usr, dept=dept)
    event.save()
    return JsonResponse({
        'title': title,
        'start': start,
        'end': end,
        'req_usr': req_usr,
        'dept': dept})


@login_required
def dashboard(request):
    '''Gets data about user's booked events and free events, and returns them
    to the dashboard.'''
    my_events = list(Event.objects.filter(username=request.user.pk).values())
    available_events = list(Event.objects.filter(username=None).values())
    return render(request, 'dashboard.html', {'my_events': my_events, 'available_events': available_events})


@login_required
def profil(request):
    '''Gets user data and returns to the profile page.'''
    user_info = CustomUser.objects.all().filter(id=request.user.pk).values()
    return render(request, 'profile.html', {'user_info': user_info})


def edit_profile(request):
    '''Allows the user to edit their profile, and saves the changes to
    the database.'''
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)
