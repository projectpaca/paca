import datetime
from django.db import models
from django.db.models import DateTimeField
from django.utils import timezone

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.contrib.contenttypes.fields import GenericRelation

from accounts.models import Department


class Event(models.Model):
    """ Grundläggande DB schema för calender """
    title = models.CharField(max_length=100)
    start = models.DateTimeField('start')
    end = models.DateTimeField('end')
    req_usr = models.PositiveIntegerField()
    dept = GenericRelation(Department)
    #dept = models.CharField(max_length=20)

    def __str__(self):
        return self.title
'''
class BookedUser(models.Model):
    """ Visar vilka anställda som är bokade på vilka pass """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = GenericForeignKey('content_type', 'CustomUser')
    # Osäker på om user "CustomUser" är korrekt, eller om den
    # behöver importeras åt något håll först?

    def __str__(self):
        return self.event
'''
