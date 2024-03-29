from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_sender = models.BooleanField()

    def __str__(self):
        return f"{self.user}"