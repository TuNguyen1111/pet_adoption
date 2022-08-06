from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class MainView(View):
    template_name = 'main_view.html'
    def get(self, request):
        return render(request, self.template_name)