from django import forms
from . import views
from django.contrib.auth.forms import UserChangeForm

# Specify that the model to use is CustomUser, and not the default user model
from userauth.models import CustomUser

class EditProfileForm(UserChangeForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = CustomUser

		fields = ['username', 'email', 'name', 'street', 'postcode', 'city', 'phone']
		exclude = []

class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'name',
            'username',
        )


