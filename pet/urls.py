from django.urls import path

from .views import HomeView, PetListView, AddPetView, SignUpView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('pets/', PetListView.as_view(), name='pet_list'),
    path('add_pet/', AddPetView.as_view(), name='add_pet'),
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
]