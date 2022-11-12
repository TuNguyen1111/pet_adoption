from django.db import models
from .user import User
from .pet import Pet


class Adoption(models.Model):
    adopter = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.OneToOneField(Pet, on_delete=models.CASCADE)
    adopt_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.adopter.username + ' - ' + self.pet.name