from django.db import models
from django.conf.urls import include, url
#from app import settings

#class Post(models.Model):
#    title = models.CharField(max_length=200)
#    author = models.ForeignKey(
#        'settings.AUTH_USER_MODEL',
#        on_delete=models.CASCADE,
#    )
#    body = models.TextField()
#
#    def __str__(self):
#        return self.title

#####
class News(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    #add in thumbnail
    #add in author

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
