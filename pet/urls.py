from django.urls import path

from .views import HomeView, PetListView, AddPetView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('pets/', PetListView.as_view(), name='pet_list'),
    path('add_pet/', AddPetView.as_view(), name='add_pet'),
]