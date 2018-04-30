from django.contrib import admin

# Register your models here.
from .models import Event
admin.site.register(Event)
    # Här har jag registrerat models.py klassen Event för att den ska vara
    # regigerbar från adminpanelen.
