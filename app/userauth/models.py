from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class CustomUserManager(UserManager):
	'''Contains all of UserManager's code which can be modified later.'''
	pass

class CustomUser(AbstractUser):
	'''Extends AbstractUser and specifies that all its objects come from the CustomUserManager.'''

	# First Name and Last Name do not cover name patterns
	# around the globe.
	username = models.CharField(
		unique=True,
		max_length=150,
	)
	email = models.EmailField(
		unique=True,
	)
	name = models.CharField(
		'Namn', 
		max_length=255,
	)
	# Employment
	empid = models.CharField(
		'Anställnings-ID', 
		max_length=20,
		unique=True,
	)
	EMP_TYPE_CHOICES = (
	    ('full time', 'Heltid'),
	    ('part time', 'Deltid'),
	    ('hourly paid', 'Timanställning'),
	    ('probationary', 'Provanställning'),
	)
	emp_type = models.CharField(
		'Anställningsform',
		max_length=20, 
		choices=EMP_TYPE_CHOICES,
		null=True,
	)

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


	#USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['empid', 'email']

	def __str__(self):
		return self.name

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





