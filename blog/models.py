from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.CharField(max_length=2500)
    image=models.ImageField(upload_to='blog/images/', blank=True)
    url = models.URLField(blank=True)