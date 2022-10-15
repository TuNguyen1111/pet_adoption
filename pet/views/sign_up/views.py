from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login

from ...forms import RegistrationForm

class SignUpView(View):
    template_name = 'registration/sign_up.html'
    form = RegistrationForm

    def get(self, request):
        context = {
            'form': self.form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            context = {
                'form': form
            }
            return render(request, self.template_name, context)