from django.contrib import admin
from .models import Adopter, Pet, Animal, PetImages

# Register your models here.
admin.site.register(Adopter)
admin.site.register(Pet)
admin.site.register(Animal)
admin.site.register(PetImages)
