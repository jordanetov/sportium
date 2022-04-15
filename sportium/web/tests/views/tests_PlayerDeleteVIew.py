from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from sportium.accounts.models import Profile
from sportium.web.models import Player

UserModel = get_user_model()


class PlayerDeleteViewTests(TestCase):
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

    VALID_PLAYER_DATA = {
        'first_name': 'Cristiano',
        'last_name': 'Ronaldo',
        'date_of_birth': '1989-02-10',
        'picture': 'https://0.academia-photos.com/111269564/26329288/24910965/s200_aleksandra.dimitrova.jpg',
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

    def __create_player_for_user(self, user):
        player = Player.objects.create(
            **self.VALID_PLAYER_DATA,
            user=user,
        )
        player.save()

        return player

    def test_delete_player__when_all_valid_expect_to_delete(self):
        user, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)

        player = self.__create_player_for_user(user)

        self.assertIsNotNone(player)
        response = self.client.delete(reverse('delete player', kwargs={'pk': player.pk}))

        self.assertEqual(response.status_code, 200)
