from django.db import models

# Create your models here.

class Card(models.Model):
    card_id = models.IntegerField()
    card_name = models.CharField(max_length=200, null=True)
    card_brand = models.CharField(max_length=30, null=True)
    card_in_out_1 = models.CharField(max_length=100, null=True)
    card_in_out_2 = models.CharField(max_length=100, null=True)
    card_in_out_3 = models.CharField(max_length=100, null=True)
    card_img = models.TextField()
    card_record = models.CharField(max_length=100, null=True)
    card_overseas = models.CharField(max_length=100, null=True)

class Benefit(models.Model):
    card_id = models.IntegerField()
    bnf_name = models.CharField(max_length=200, null=True)
    bnf_content = models.TextField(null=True)
    bnf_detail = models.TextField(null=True)