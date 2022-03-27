from django.urls import path

from sportium.web.views import HomeView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
)

