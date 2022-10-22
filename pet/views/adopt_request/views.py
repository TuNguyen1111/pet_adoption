from django.shortcuts import render
from django.views import View


class AdoptRequestView(View):
    template = 'adopt_request.html'

    def get(self, request):
        return render(request, self.template)