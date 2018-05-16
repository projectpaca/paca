from django.contrib import admin

# Register your models here.
from .models import Department, UserInDepartment
admin.site.register(Department, UserInDepartment)
