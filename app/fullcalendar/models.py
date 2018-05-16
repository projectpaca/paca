import datetime
from django.db import models
from django.db.models import DateTimeField
from django.utils import timezone


class Event(models.Model):
    """ Grundläggande DB schema för calender """
    title = models.CharField(max_length=100)
    start = models.DateTimeField('start')
    end = models.DateTimeField('end')
    req_usr = models.int()

    def __str__(self):
        return self.title

class BookedUser(models.Model):
    """ Visar vilka anställda som är bokade på vilka pass """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Osäker på om user "CustomUser" är korrekt, eller om den
    # behöver importeras åt något håll först?

    def __str__(self):
        return self.title
