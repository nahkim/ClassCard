from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
TAG_CHOICES = {
    ('YEAR','연말정산'),
    ('NEWS','뉴스'),
    ('RECOMMEND','추천·리뷰'),
    ('BASIC','기초상식'),
    ('BODO','보도자료'),
}
# Create your models here.
class Magazine(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='image/mzimg')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tag = models.CharField(max_length=20, verbose_name='태그명', choices=TAG_CHOICES)

    # 유저가 없어서 현재는 작성이 안됩니당
    # 다중이미지 고려..
    # 에디터 가지고 오시죠...

class Comment(models.Model):
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE,related_name='recomment',null=True)
    grade = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)

    