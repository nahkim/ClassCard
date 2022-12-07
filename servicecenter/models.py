from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class ServiceQuestion(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class ServiceComment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    quest = models.ForeignKey(ServiceQuestion, on_delete=models.CASCADE)