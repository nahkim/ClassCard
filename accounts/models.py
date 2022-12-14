from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ("U", "User"),
        ("C", "Critic"),
    ]

    nickname = models.CharField(max_length=10, unique=True)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default="U")
    profile = models.ImageField(upload_to="images", blank=True, null=True)
    follow = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers", blank=True
    )

    def save(self, *args, **kwargs):
        if self.nickname is "":
            self.nickname = self.username
        super(User, self).save(*args, **kwargs)
