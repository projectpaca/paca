from django.contrib.auth.models import AbstractUser, UserManager

class CustomUserManager(UserManager):
	'''Contains all of UserManager's code which can be modified later.'''
	pass

class CustomUser(AbstractUser):
	'''Extends AbstractUser and specifies that all its objects come from the CustomUserManager.'''
	objects = CustomUserManager()

  
