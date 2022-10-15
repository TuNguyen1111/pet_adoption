from django.db import models
from .user import User
from .animals import Animal
# Create your models here.

class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    is_adopted = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name