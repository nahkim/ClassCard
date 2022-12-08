from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

rate_choice = (
    ('1', '⭐'),
    ('2', '⭐⭐'),
    ('3', '⭐⭐⭐'),
    ('4', '⭐⭐⭐⭐'),
    ('5', '⭐⭐⭐⭐⭐'),
  )

class Card(models.Model):
    card_name = models.CharField(max_length=200, null=True)
    card_brand = models.CharField(max_length=30, null=True)
    card_in_out_1 = models.CharField(max_length=100, null=True)
    card_in_out_2 = models.CharField(max_length=100, null=True)
    card_in_out_3 = models.CharField(max_length=100, null=True)
    card_img = models.TextField()
    card_record = models.CharField(max_length=100, null=True)
    card_overseas = models.CharField(max_length=100, null=True)

class Benefit(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True)
    bnf_name = models.CharField(max_length=200, null=True)
    bnf_content = models.TextField(null=True)
    bnf_detail = models.TextField(null=True)

class DetailComment(models.Model):
    content = models.TextField()
    rate = models.CharField(max_length=10, choices=rate_choice)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)