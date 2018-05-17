from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Department(models.Model):
    """ Företagets avdelningar """
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    # Below the mandatory fields for generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey()

    def __str__(self):
        return self.name

'''
class UserInDepartment(models.Model):
    """ Vilka personer som jobbar i vilka avdelningar """
    dep =  # FK
    user = # FK

    def __str__(self):
        return self.dep
        '''
