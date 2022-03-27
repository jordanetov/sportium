from django.shortcuts import render

# Create your views here.
from django.views import generic as views


class HomeView(views.TemplateView):
    template_name = 'web/home_page.html'


class AboutView(views.TemplateView):
    template_name = 'web/about_page.html'
