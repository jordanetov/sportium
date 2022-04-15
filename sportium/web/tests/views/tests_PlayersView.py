from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from sportium.accounts.models import Profile
from sportium.web.models import Player

UserModel = get_user_model()


class PlayersViewTests(TestCase):
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

    def __get_response_for_players(self, user):
        return self.client.get(reverse('players', kwargs={'pk': user.pk}))

    def test_shows_correct_template_and_message__when_no_players(self):
        user, profile = self.__create_valid_user_and_profile()
        self.__get_response_for_players(user)
        self.assertTemplateUsed('web/players.html')

    def test_when_no_players__expect_total_players_count_to_be_0(self):
        user, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)

        response = self.__get_response_for_players(user)

        self.assertEqual(0, len(response.context['players']))

    def test_when_players__expect_total_players_count_to_be_correct(self):
        user, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)

        self.__create_player_for_user(user)
        self.__create_player_for_user(user)

        response = self.__get_response_for_players(user)

        self.assertEqual(2, len(response.context['players']))
