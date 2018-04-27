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
	    max_length=12, 
	    )

	# Employment
	empid = models.IntegerField(
		'Anställnings-ID', 
		max_length=None,
		primary_key=True,
		)
	EMP_TYPE_CHOICES = (
	        ('full time', 'heltid'),
	        ('part time', 'deltid'),
	        ('extra', 'extrajobb')
	        ('probationary', 'provanställning')
	    )
	emp_type = models.CharField(max_length=1, choices=EMP_TYPE_CHOICES)
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
	phone = models.IntegerField(
		'Telefonnummer', 
		max_length=20, 
		blank=True,
		)

class EmergencyContacts():
	''''''
	# References CustomUser and is deleted if FK is deleted
	employee = models.ForeignKey('CustomUser', on_delete=CASCADE)



