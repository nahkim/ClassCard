from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

rate_choice = (
    ('1', '⭐'),
    ('2', '⭐⭐'),
    ('3', '⭐⭐⭐'),
    ('4', '⭐⭐⭐⭐'),
    ('5', '⭐⭐⭐⭐⭐'),
  )


TAG_CHOICES = {
    ("YEAR", "연말정산"),
    ("NEWS", "뉴스"),
    ("RECOMMEND", "추천·리뷰"),
    ("BASIC", "기초상식"),
    ("BODO", "보도자료"),
    ("ECT", "기타"),
}
# Create your models here.
class Magazine(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="image/mzimg")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tag = models.CharField(
        max_length=20, verbose_name="태그명", choices=TAG_CHOICES, default="ECT"
    )
    bookmark_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="bookmark_articles"
    )


class Comment(models.Model):
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="recomment", null=True
    )
    grade = models.CharField(
        max_length=10, choices=rate_choice
    )
