from django.contrib import admin

# Register your models here.
from .models import Event, Department
# admin.site.register(Event)
# Här har jag registrerat models.py klassen Event för att den ska vara
# regigerbar från adminpanelen.
admin.site.register(Department)
# Är inte dessa i separata .register() så orsakar det error:
# AttributeError: 'Department' object has no attribute 'urls'


@admin.register(Event)
class myEvent(admin.ModelAdmin):
    list_display = ('skift', 'start', 'end', 'username')

    def skift(self, obj):
        return obj.title.name

"""

class UserAdmin(admin.ModelAdmin):
    list_display = (..., 'get_author')

    def get_author(self, obj):
        return obj.book.author
    get_author.short_description = 'Author'
    get_author.admin_order_field = 'book__author'



class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

class Department(models.Model):
    name = models.CharField(
        max_length=100,
        primary_key=True
        )
    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.ForeignKey(
        Department,
        on_delete=models.CASCADE    )
    start = models.DateTimeField('start')
    end = models.DateTimeField('end')
    # booked = models.ForeignKey('User', on_delete=models.CASCADE)
    username = models.ForeignKey(
"""
