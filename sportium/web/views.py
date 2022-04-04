from django.urls import reverse_lazy
from django.views import generic as views

from sportium.web.forms import RegisterPlayerForm
from sportium.web.models import Club, Player


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


class ClubDetailsView(views.DetailView):
    model = Club
    template_name = 'web/club_details.html'
    context_object_name = 'club'

    def get_context_data(self, **kwargs):
        players = Player.objects.filter(id=self.object.id)
        context = super().get_context_data(**kwargs)

        players_count = len(players)

        context.update({
            'players': players,
            'players_count': players_count,
        })

        return context


class PlayersView(views.ListView):
    model = Player
    template_name = 'web/players.html'
    context_object_name = 'players'

    def get_queryset(self):
        return Player.objects.filter(
            user_id=self.request.user.id
        )


class PLayerRegisterView(views.CreateView):
    template_name = 'web/register_player.html'
    form_class = RegisterPlayerForm
    success_url = reverse_lazy('clubs')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

    # we are giving the argument 'user' that we have put in the form (CreatePetForm)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
