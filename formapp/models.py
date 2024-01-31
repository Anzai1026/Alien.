from django.db import models
import datetime
class PostModel(models.Model):
    author = models.CharField(max_length=64, null=True)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    title = models.CharField(max_length=32)
    published_date = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now())

