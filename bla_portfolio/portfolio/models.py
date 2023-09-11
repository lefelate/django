from django.db import models


# Create your models here.

class Blogs(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    authname = models.CharField(max_length=50)
    img = models.ImageField(upload_to='blog', blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
