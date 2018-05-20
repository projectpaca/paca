from django import forms
from django.http import HttpRequest
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser, EmergencyContacts


# class EmergencyContactsInline(admin.TabularInline):
#     model = EmergencyContacts


class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser


class MyUserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update(
        {
            'duplicate_username': 'This username har already been taken.',
            'duplicate_email': 'This email has already been taken.',
            'duplicate_empid': 'This employee ID has already been taken.',
        }
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        #fields = UserCreationForm.Meta.fields + ('name', 'empid', 'emp_type',)

    def clean_name(self):
        name = self.cleaned_data['name']
        try:
            CustomUser.objects.get(name=name)
        except CustomUser.DoesNotExist:
            return name

        raise forms.ValidationError(self.error_messages['duplicate_username'])
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return username

        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return email

        raise forms.ValidationError(self.error_messages['duplicate_email'])

    def clean_empid(self):
        empid = self.cleaned_data['empid']
        try:
            CustomUser.objects.get(empid=empid)
        except CustomUser.DoesNotExist:
            return empid

        raise forms.ValidationError(self.error_messages['duplicate_empid'])


@admin.register(CustomUser)
class MyUserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm

    # def get_emergency_contacts(request):
    #     '''Gets the emergency contacts of the current user.'''
    #     emergency_contacts = EmergencyContacts.objects.filter(user_reference=request.user.username)
    #     return emergency_contacts

    fieldsets = (
        ('User Profile',
            {'fields': (
                'name',
                'username',
                'email',
                'empid',
                'emp_type',
                'password',
                )
            }
        ),
        ('Personal info',
            {'fields': (
                'phone',
                'street',
                'postcode',
                'city',
                )
            }
        ),
        # ('Emergency Contacts',
        #     {'fields': (
        #         'emergency_contacts.name',
        #         'emergency_contacts.relationship',
        #         'emergency_contacts.phone',
        #         ) 
        #     }
        # ),
        ('Permissions',
            {'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
                )
            }
        ),
        ('Important dates',
            {'fields': (
                'last_login',
                'date_joined',
                )
            }
        ),

    )
    # inlines = [EmergencyContactsInline]
    list_display = ('empid', 'name', 'emp_type', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ['name']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'name', 'email', 'empid', 'emp_type', 'password1', 'password2')}),)


