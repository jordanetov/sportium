from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from sportium.accounts.models import Profile

UserModel = get_user_model()


class ProfileLogoutViewTests(TestCase):
    VALID_USER_CREDENTIALS = {
        'username': 'test',
        'password': '1234',
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Jordan',
        'last_name': 'Etov',
        'date_of_birth': '1989-02-10',
        'personal_information': 'Some guy',
        'picture': 'https://0.academia-photos.com/111269564/26329288/24910965/s200_aleksandra.dimitrova.jpg',
        'email': 'jordy@abv.bg',
        'gender': 'Prefer not to say',
    }

    @staticmethod
    def __create_user(**credentials):
        return UserModel.objects.create_user(**credentials)

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )

        return user, profile

    def test_logout_user__expect_to_redirect_to_login(self):
        self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)

        response = self.client.get(
            reverse('logout'),
        )

        self.assertEquals(response.status_code, 302)
