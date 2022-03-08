from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    date = models.DateField(blank=True)

    def __str__(self):
        return self.title