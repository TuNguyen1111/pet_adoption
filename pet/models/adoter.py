from django.db import models


class Adopter(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=300)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self) -> str:
        return self.full_name

    @property
    def full_name(self) -> str:
        return self.last_name + self.first_name
