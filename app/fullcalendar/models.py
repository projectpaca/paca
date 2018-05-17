import datetime
from django.db import models
from django.db.models import DateTimeField
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class Department(models.Model):
    """ Företagets avdelningar """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    """ Grundläggande DB schema för calender """
    title = models.ForeignKey(Department, on_delete=models.CASCADE)
    start = models.DateTimeField('start')
    end = models.DateTimeField('end')
    # booked = models.ForeignKey('User', on_delete=models.CASCADE)
    username = models.ForeignKey(
        get_user_model(),
        null=True,
        on_delete=models.CASCADE
    )

    # booked = bokad på användare #

    def __str__(self):
        return self.title
