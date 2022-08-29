from django.shortcuts import render, redirect
from django.views import View

from ...forms import PetForm

class AddPetView(View):
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