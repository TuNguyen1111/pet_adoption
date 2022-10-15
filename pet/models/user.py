from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    address = models.CharField(max_length=300)
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self) -> str:
        return self.full_name

    @property
    def full_name(self) -> str:
        return self.last_name + self.first_name
