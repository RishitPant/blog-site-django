from django.db import models
from datetime import datetime
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, default='')
    subtitle = models.CharField(max_length=50, default='')
    author = models.CharField(max_length=15, default='')
    post = RichTextUploadingField(blank=True, null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
   
    def __str__(self):
        return str(self.title) + " | " + str(self.author)


class Contacts(models.Model):
    name = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=15, default='')
    phone = models.CharField(max_length=13, default='')
    message = models.TextField(max_length=10000, default='')
    date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return  "Message from " + self.name