from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser


class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser


class MyUserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update(
        {
            "duplicate_email": "This email has already been taken.",
            "duplicate_empid": "This employee ID has already been taken.",
        }
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        #fields = UserCreationForm.Meta.fields + ("name", "empid", "emp_type",)

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return email

        raise forms.ValidationError(self.error_messages["duplicate_email"])

    def clean_empid(self):
        empid = self.cleaned_data["empid"]
        try:
            CustomUser.objects.get(empid=empid)
        except CustomUser.DoesNotExist:
            return empid

        raise forms.ValidationError(self.error_messages["duplicate_empid"])



@admin.register(CustomUser)
class MyUserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = (
        ("User Profile", 
            {"fields": (
                "name",
                "email",
                "empid", 
                "emp_type", 
                "password",
                )
            }
        ),
        ("Personal info",
            {"fields": (
                "phone",
                "street",
                "postcode",
                "city", 
                )
            }
        ),
        ("Permissions",
            {"fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups", 
                "user_permissions",
                )
            }
        ),
        ("Important dates",
            {"fields": (
                "last_login",
                "date_joined",
                )

            }
        )
    )
    list_display = ("name", "empid", "emp_type", "is_superuser")
    search_fields = ["name"]
    add_fieldsets = (
        (None, {
            'classes': ("wide",),
            'fields': ("name", "email", "empid", "emp_type", "password1", "password2")}),)
