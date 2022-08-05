from django.urls import path

from .views import HomeView, PetListView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('pets/', PetListView.as_view(), name='pet_list'),
]