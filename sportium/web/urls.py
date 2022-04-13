from django.urls import path

from sportium.web.views import HomeView, AboutView, ContactView, ClubsView, PlayersView, ClubDetailsView, \
    PLayerRegisterView, delete_player, thanks_view, EventsView, no_permission_view

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('thanks/', thanks_view, name='thanks'),
    path('no-permission/', no_permission_view, name='no permission'),

    path('clubs/', ClubsView.as_view(), name='clubs'),
    path('clubs/<int:pk>/', ClubDetailsView.as_view(), name='club info'),

    path('players/<int:pk>/', PlayersView.as_view(), name='players'),
    path('player/register/', PLayerRegisterView.as_view(), name='register player'),
    path('player/delete/<int:pk>/', delete_player, name='delete player'),

    path('events/', EventsView.as_view(), name='events'),
)
