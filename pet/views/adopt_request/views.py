from django.shortcuts import render, get_object_or_404
from django.views import View

from ...forms import AdoptRequestForm
from ...models import Pet

class AdoptRequestView(View):
    template = 'adopt_request.html'
    form = AdoptRequestForm

    def get(self, request, pet_id):
        pet = get_object_or_404(Pet, pk=pet_id)
        user = request.user
        initial = {
            'pet_name': pet.name,
            'animal_type': pet.animal.name,
        }

        if user:
            initial.update({
                'adopter_first_name': user.first_name,
                'adopter_last_name': user.last_name,
                'adopter_age': user.age,
                'adopter_address': user.address,
            })

        form = self.form(initial=initial)
        context = {
            'form': form
        }

        return render(request, self.template, context)