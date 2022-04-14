from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from sportium.accounts.models import Profile
from sportium.web.models import Player

UserModel = get_user_model()


class ProfileTests(TestCase):
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

    def test_player_create__when_first_name_contains_only_letters__expect_success(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        player = self.__create_player_for_user(user)

        player.save()
        self.assertIsNotNone(player.pk)

    def test_player_create__when_first_name_contains_a_digit__expect_to_fail(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        player = self.__create_player_for_user(user)
        player.first_name = 'Jordan1'

        with self.assertRaises(ValidationError) as context:
            player.full_clean()
            player.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_hashtag_sign__expect_to_fail(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        player = self.__create_player_for_user(user)
        player.first_name = 'Jor#an'

        with self.assertRaises(ValidationError) as context:
            player.full_clean()
            player.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_space__expect_to_fail(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        player = self.__create_player_for_user(user)
        player.first_name = 'Jord an'

        with self.assertRaises(ValidationError) as context:
            player.full_clean()
            player.save()

        self.assertIsNotNone(context.exception)
