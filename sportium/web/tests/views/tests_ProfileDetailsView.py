from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from sportium.accounts.models import Profile
from sportium.web.models import Player

UserModel = get_user_model()


class ProfileDetailsTests(TestCase):
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

    def __get_response_for_profile(self, profile):
        return self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))

    def __create_player_for_user(self, user):
        player = Player.objects.create(
            **self.VALID_PLAYER_DATA,
            user=user,
        )
        player.save()

        return player


    def test_when_opening_not_existing_profile__expect_404_actual_302(self):
        response = self.client.get(reverse('profile details', kwargs={
            'pk': 141315,
        }))

        self.assertEqual(302, response.status_code)

    def test_profile_details__when_profile_exists_expect_success(self):
        _, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)

        response = self.__get_response_for_profile(profile)
        actual_profile = response.context['object']

        self.assertEqual(profile, actual_profile)

    def test_expect_correct_template(self):
        _, profile = self.__create_valid_user_and_profile()
        self.__get_response_for_profile(profile)
        self.assertTemplateUsed('accounts/profile_details.html')

    def test_when_user_is_owner__expect_is_owner_to_be_true(self):
        _, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)

        response = self.__get_response_for_profile(profile)

        self.assertTrue(response.context['is_owner'])

    def test_when_user_is_not_owner__expect_is_owner_to_be_false(self):
        _, profile = self.__create_valid_user_and_profile()
        credentials = {
            'username': 'test2',
            'password': '12',
        }

        self.__create_user(**credentials)
        self.client.login(**credentials)
        response = self.__get_response_for_profile(profile)

        self.assertFalse(response.context['is_owner'])

    def test_when_no_players__expect_total_players_count_to_be_0(self):
        user, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)

        response = self.__get_response_for_profile(profile)

        self.assertEqual(0, response.context['players_count'])

    def test_when_player_created__expect_total_players_count_to_be_1(self):
        user, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)

        self.__create_player_for_user(user)
        response = self.__get_response_for_profile(profile)

        self.assertEqual(1, response.context['players_count'])

    def test_when_user_has_players__expect_to_return_only_users_players(self):
        user, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)

        credentials = {
            'username': 'test2',
            'password': '12',
        }
        user2 = self.__create_user(**credentials)

        player = self.__create_player_for_user(user)
        self.__create_player_for_user(user2)

        response = self.__get_response_for_profile(profile)

        self.assertListEqual(
            [player],
            list(response.context['players']),
        )

    def test_when_user_has_no_players__players_should_be_empty(self):
        _, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)

        response = self.__get_response_for_profile(profile)
        self.assertListEqual(
            [],
            list(response.context['players']),
        )
