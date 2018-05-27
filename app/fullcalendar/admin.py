from django.contrib import admin
from .models import Event, Department


admin.site.register(Department)


@admin.register(Event)
class myEvent(admin.ModelAdmin):
    """
    Visar modellen "Event" på adminportalen, och listar upp list_display
    som kolumner så att man får mer information än bara PK.
    """
    list_display = ('skift', 'start', 'end', 'username')

    def skift(self, obj):
        return obj.title.name
