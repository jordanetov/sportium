from django.urls import path

from sportium.web.views import HomeView, AboutView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
)

