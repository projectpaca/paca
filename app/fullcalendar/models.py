import datetime
from django.db import models
from django.db.models import DateTimeField
from django.utils import timezone


class Event (models.Model):
    """ Grundläggande DB schema för calender """
    # Gör table för vem som är bokad på vilket pass
    title = models.CharField(max_length=100)
    start = models.DateTimeField('start')
    end = models.DateTimeField('end')
        # models.CharField(max_length=20)
    # Antal platser på passet


    def __str__(self):
        # It’s important to add __str__() methods to your models, not only for your
        # own convenience when dealing with the interactive prompt, but also
        # because objects’ representations are used throughout Django’s
        # automatically-generated admin.
        return self.title

    #def shift_is_this_week (self):
    #    return self.start timezone.now() <= datetime.timedelta(days=7)
    #    TypeError: unorderable types: datetime.datetime() <= datetime.timedelta()

    #https://docs.djangoproject.com/en/2.0/intro/tutorial03/
    #https://docs.google.com/document/d/1_l-36sKyUWxNda1w3_TgmYIuzPVrlPftkxqQYeC7_6A/edit
    #
