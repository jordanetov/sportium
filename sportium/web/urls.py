from django.urls import path

from sportium.web.views import HomeView, AboutView, ContactView, ClubsView, PlayersView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('clubs/', ClubsView.as_view(), name='clubs'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('players/<int:pk>/', PlayersView.as_view(), name='players'),
)
