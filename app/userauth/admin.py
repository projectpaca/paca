# Import existing UserAdmin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Import custom made forms and user model
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
	'''Tells the admin site to use the new CustomUser model.'''
	model = CustomUser
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm

admin.site.register(CustomUser, CustomUserAdmin)