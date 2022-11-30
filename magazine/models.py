from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Magazine(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='image/mzimg')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # 유저가 없어서 현재는 작성이 안됩니당
    # 다중이미지 고려..

class Comment(models.Model):
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE,related_name='recomment',null=True)
    grade = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)

    