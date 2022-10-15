from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from ...forms import PetForm


# TODO: set permission for user who can add new pet
class AddPetView(LoginRequiredMixin, View):
    login_url = '/login'
    template_name = 'add_pet.html'
    form = PetForm

    def get(self, request):
        form = self.form

        context = {
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('add_pet')