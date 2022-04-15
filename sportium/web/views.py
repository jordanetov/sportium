from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from sportium.web.forms import RegisterPlayerForm, DelPlayerForm, ContactsForm
from sportium.web.models import Club, Player, Contacts, Event


def thanks_view(request):
    return render(request, 'web/thanks_message.html')


def no_permission_view(request):
    return render(request, 'web/no_permission.html')


class HomeView(views.TemplateView):
    template_name = 'web/home_page.html'


class AboutView(views.TemplateView):
    template_name = 'web/about_page.html'


class ContactView(views.CreateView):
    model = Contacts
    form_class = ContactsForm
    success_url = reverse_lazy('thanks')
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
    # user = Player.user
    template_name = 'web/register_player.html'
    form_class = RegisterPlayerForm
    success_url = reverse_lazy('clubs')

    def get_success_url(self):
        # return reverse_lazy('profile details', kwargs={'pk': self.object.id})
        if self.success_url:
            return self.success_url
        return super().get_success_url()

    # we are giving the argument 'user' that we have put in the form
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


def delete_player(request, pk):
    user = request.user
    player = Player.objects.get(pk=pk)
    if request.method == 'POST':
        form = DelPlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            messages.info(request, 'The player has been deleted.')
            return redirect('players', user.id)
    else:
        form = DelPlayerForm(instance=Player.objects.get(pk=pk))

    context = {
        'form': form,
        'player': player,
    }

    return render(request, 'web/delete_player.html', context)


class EventsView(views.ListView):
    model = Event
    template_name = 'web/events.html'
    context_object_name = 'events'
