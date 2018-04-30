from django.db import models

# Create your models here.

class Event (models.Model):
    """ Grundläggande DB schema för calender """
    start = models.datetime()
    end = models.datetime()
    title = models.CharField(max_length=100)
