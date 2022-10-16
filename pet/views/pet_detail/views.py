from django.views.generic.detail import DetailView

from ...models import Pet


class PetDetailView(DetailView):
    template_name = 'pet_detail.html'
    model = Pet