# Import existing Django forms in order to extend them
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Specify that the model to use is CustomUser, and not the default user model
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
	'''
        Subclasses the existing UserCreationForm and specifying it to use our
        new CustomUser model.
        '''

	class Meta(UserCreationForm.Meta):
		model = CustomUser
		fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):
	'''
        Subclasses the existing UserChangeForm and specifying it to use
        our new CustomUser model.
        '''

	class Meta:
		model = CustomUser
		fields = UserChangeForm.Meta.fields
