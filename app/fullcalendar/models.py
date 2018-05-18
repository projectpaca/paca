import datetime
from django.db import models
from django.db.models import DateTimeField
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings


class Department(models.Model):
    """ Företagets avdelningar """
    name = models.CharField(
        verbose_name="namn",
        max_length=100,
        primary_key=True
        )

    def __str__(self):
        return self.name


class Event(models.Model):
    """ Grundläggande DB schema för calender """
    title = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
    start = models.DateTimeField('start')
    end = models.DateTimeField('end')
    username = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title.name

    def Meta(self):
        verbose_name="Skift"
