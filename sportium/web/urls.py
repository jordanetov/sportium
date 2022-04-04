from django.urls import path

from sportium.web.views import HomeView, AboutView, ContactView, ClubsView, PlayersView, ClubDetailsView, \
    PLayerRegisterView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactView.as_view(), name='contacts'),

    path('clubs/', ClubsView.as_view(), name='clubs'),
    path('clubs/<int:pk>/', ClubDetailsView.as_view(), name='club info'),

    path('players/<int:pk>/', PlayersView.as_view(), name='players'),
    path('player/register/', PLayerRegisterView.as_view(), name='register player'),
)
