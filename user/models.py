from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    country = models.CharField(default="", max_length=64)

    class Meta:
        managed = True
        db_table = 'Users'

    def __str__(self) -> str:
        return self.username
