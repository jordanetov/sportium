from django.urls import path

from sportium.accounts.views import UserRegisterView, UserLoginView, UserLogoutView, ProfileDetailsView, \
    EditProfileView, delete_user

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('edit/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('delete/', delete_user, name='delete profile'),
)
