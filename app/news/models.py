from django.db import models
from django.conf.urls import include, url
from app import settings
from userauth.models import CustomUser

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
	author = models.ForeignKey(
		CustomUser,
		'Författare',
		null=True,
	)
	title = models.CharField(
		'Rubrik',
		max_length=100,
	)
	#slug = models.SlugField()
	content = models.TextField(
		'Brödtext',
	)
	date = models.DateTimeField(
		auto_now_add=True, 
		null=True, 
		blank=True
	)

	list_display = ('title', 'author', 'date')
	search_fields = ['title','author','date']
	list_filter = ['author','date']

	class Meta:
	        verbose_name = 'nyhet'
	        verbose_name_plural = 'nyheter'

	def __str__(self):
		return self.title

<<<<<<< HEAD
=======
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
>>>>>>> lisa
