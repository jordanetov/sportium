from django.shortcuts import render

# Create your views here.
from django.views import generic as views

from sportium.web.models import Club


class HomeView(views.TemplateView):
    template_name = 'web/home_page.html'


class AboutView(views.TemplateView):
    template_name = 'web/about_page.html'


class ContactView(views.TemplateView):
    template_name = 'web/contacts.html'


class ClubsView(views.ListView):
    model = Club
    template_name = 'web/clubs.html'
    context_object_name = 'clubs'
