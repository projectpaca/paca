from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class CustomUserManager(UserManager):
	'''Contains all of UserManager's code which can be modified later.'''
	pass

class CustomUser(AbstractUser):
	'''Extends AbstractUser and specifies that all its objects come from the CustomUserManager.'''
	objects = CustomUserManager()

	# Identifiers
	pnr = models.IntegerField(
		'Personnummer', 
	    blank=True,
	    help_text='Format: ååååmmddnnnn' 
	    )

	# Employment
	empid = models.CharField(
		'Anställnings-ID', 
		max_length=20,
		)
	EMP_TYPE_CHOICES = (
	        ('full time', 'heltid'),
	        ('part time', 'deltid'),
	        ('hourly paid', 'timanställning'),
	        ('probationary', 'provanställning'),
	    )
	emp_type = models.CharField(
		max_length=20, 
		choices=EMP_TYPE_CHOICES,
		null=True)
    # emp_date = join_date (default)

    # Contact
	street = models.CharField(
    	'Gatunamn och -nummer', 
    	max_length=100, 
    	blank=True,
    	)
	postcode = models.CharField(
		'Postnummer', 
		max_length=5, 
		blank=True,
		)
	city = models.CharField(
		'Ort', 
		max_length=50, 
		blank=True,
		)
	phone = models.CharField(
		'Telefonnummer', 
		max_length=20, 
		blank=True,
		)

# class EmergencyContacts():
# 	''''''
# 	# References CustomUser and is deleted if FK is deleted
# 	empid_f = models.ForeignKey('CustomUser', on_delete=CASCADE)


# class LangComp():
# 	''''''
# 	empid_f = models.ForeignKey('CustomUser', on_delete=CASCADE)
# 	LANGUAGE_CHOICES = (
# 		('')
# 		)
# 	language = models.CharField(choices=LANGUAGE_CHOICES)





