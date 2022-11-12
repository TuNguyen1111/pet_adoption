from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages

from ...forms.user_profile import UserProfileForm


class UserProfileView(View):
    template = 'user_profile.html'
    form = UserProfileForm

    def get(self, request):
        user = self.request.user
        context = {
            'form': self.form(instance=user)
        }
        return render(request, self.template, context)

    def post(self, request):
        # add instance for update
        form = self.form(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update success!')
        return redirect('user_profile')
            