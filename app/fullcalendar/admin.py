from django.contrib import admin

# Register your models here.
from .models import Event, Department
admin.site.register(Event)
# Här har jag registrerat models.py klassen Event för att den ska vara
# regigerbar från adminpanelen.
admin.site.register(Department)
# Är inte dessa i separata .register() så orsakar det error:
# AttributeError: 'Department' object has no attribute 'urls'
