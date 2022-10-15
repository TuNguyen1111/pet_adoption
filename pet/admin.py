from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Pet, Animal, PetImages

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Pet)
admin.site.register(Animal)
admin.site.register(PetImages)
