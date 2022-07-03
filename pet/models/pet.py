from django.db import models
from .adoter import Adopter
from .animals import Animal
# Create your models here.

class Pet(models.Model):
    adopter = models.ForeignKey(Adopter, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    is_adopted = models.BooleanField(default=False)
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self) -> str:
        return self.name