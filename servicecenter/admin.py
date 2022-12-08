from django.contrib import admin
from .models import ServiceQuestion, ServiceComment
# Register your models here.
admin.site.register(ServiceQuestion)
admin.site.register(ServiceComment)