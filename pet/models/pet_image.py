from django.db import models
from .pet import Pet

class PetImages(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self) -> str:
        return self.pet.name + '_image'