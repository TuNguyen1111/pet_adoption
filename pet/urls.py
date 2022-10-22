from django.urls import path

from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('pets/', PetListView.as_view(), name='pet_list'),
    path('add_pet/', AddPetView.as_view(), name='add_pet'),
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('pet_detail/<int:pk>', PetDetailView.as_view(), name='pet_detail'),
    path('adopt_request/', AdoptRequestView.as_view(), name='adopt_request'),
]