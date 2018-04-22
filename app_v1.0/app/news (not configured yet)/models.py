from django.db import models
from app import settings

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'settings.AUTH_USER_MODEL',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title