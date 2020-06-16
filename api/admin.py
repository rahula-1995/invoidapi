from django.contrib import admin

# Register your models here.
from .models import imageapi,responseapi

admin.site.register(imageapi)
admin.site.register(responseapi)
