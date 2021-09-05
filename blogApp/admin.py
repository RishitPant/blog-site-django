from django.contrib import admin
from .models import Post
from blogApp.models import Contacts

# Register your models here.
admin.site.register(Post)
admin.site.register(Contacts)
