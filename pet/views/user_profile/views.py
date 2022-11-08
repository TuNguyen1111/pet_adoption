from django.views import View
from django.shortcuts import render

from ...forms.user_profile import UserProfileForm


class UserProfileView(View):
    template = 'user_profile.html'
    form = UserProfileForm

    def get(self, request):
        context = {
            'form': self.form
        }
        return render(request, self.template, context)