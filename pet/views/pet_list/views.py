from django.shortcuts import render
from django.views.generic.list import ListView

from ...models.pet import Pet


class PetListView(ListView):
    model = Pet
    template_name = 'pet_list.html'