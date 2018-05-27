import datetime
from django.db import models
from django.db.models import DateTimeField
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings
from userauth.models import CustomUser


class Department(models.Model):
    '''A database model for a company's departments.'''
    name = models.CharField(
        'Namn',
        max_length=100,
        primary_key=True
        )
    supervisor = models.ForeignKey(
        CustomUser,
        'Ansvarig',
        limit_choices_to={'is_staff': True},
        null=True,
    )
    description = models.TextField(
        'Beskrivning',
        blank=True,
    )

    list_display = ('name', 'supervisor')
    search_fields = ['name', 'supervisor']
    list_filter = ['name', 'supervisor']

    class Meta:
        verbose_name = 'avdelning'
        verbose_name_plural = 'avdelningar'

    def __str__(self):
        return self.name


class Event(models.Model):
    '''Database model for a calendar event (shift).'''
    title = models.ForeignKey(
        Department,
        'Titel',
    )
    start = models.DateTimeField('start')
    end = models.DateTimeField('slut')
    username = models.ForeignKey(
        get_user_model(),
        limit_choices_to={'is_active': True},
        null=True,
        blank=True,
        verbose_name="Bokad på",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'pass'
        verbose_name_plural = 'pass'

    def __str__(self):
        return self.title.name
