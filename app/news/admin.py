from django.contrib import admin
from .models import News


# Registers News model to the admin portal
admin.site.register(News)
