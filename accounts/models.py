from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ('U', 'User'),
        ('A', 'Admin'),
    ]

    nickname = models.CharField(max_length=10)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)
    profile = models.ImageField(
        upload_to='images'
    )
    follow = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )