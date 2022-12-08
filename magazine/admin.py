from django.contrib import admin

# Register your models here.
from .models import Magazine, Comment

admin.site.register(Magazine)
admin.site.register(Comment)