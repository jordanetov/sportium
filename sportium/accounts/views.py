from django.contrib import messages
from django.contrib.auth import views as auth_views, authenticate, login
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from sportium.accounts.forms import CreateProfileForm, DelProfileForm
from sportium.common.mixins import RedirectToHomeMixin
from sportium.accounts.models import Profile
from sportium.web.models import Player


class UserRegisterView(RedirectToHomeMixin, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # save the new user first
        form.save()
        # authenticate user then login
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'], )
        login(self.request, user)
        return HttpResponseRedirect(reverse('home'))


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    def get_next_page(self):
        return reverse_lazy('login')


class ProfileDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        players = Player.objects.filter(user_id=self.object.user_id)
        context = super().get_context_data(**kwargs)

        players_count = len(players)

        context.update({
            'players': players,
            'players_count': players_count,
            'is_owner': self.object.user_id == self.request.user.id,
        })

        return context


class EditProfileView(views.UpdateView):
    model = Profile
    template_name = 'accounts/edit_profile.html'
    fields = ('first_name', 'last_name', 'date_of_birth', 'personal_information', 'picture', 'email',)

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.user_id})


# class DelProfileView(views.DeleteView):
#     model = Profile
#     template_name = 'accounts/delete_profile.html'
#     success_url = reverse_lazy('home')

@login_required
def delete_user(request):
    user = request.user
    if request.method == 'POST':
        form = DelProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your account has been deleted.')
            return redirect('home')
    else:
        form = DelProfileForm(instance=request.user)

    context = {
        'form': form,
        'user': user,
    }

    return render(request, 'accounts/delete_profile.html', context)
