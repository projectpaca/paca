from django.contrib import admin
from .models import Event, Department


# Registers Department model to the admin portal
admin.site.register(Department)


@admin.register(Event)
class myEvent(admin.ModelAdmin):
    '''Displays the model "Event" in the admin portal, 
    and lists the fields in list_display.'''
    list_display = ('skift', 'start', 'end', 'username')

    def skift(self, obj):
        return obj.title.name
