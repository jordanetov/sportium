from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from sportium.accounts.models import Profile
from sportium.web.models import Player, Club

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

    VALID_CLUB_DATA = {
        'name': 'Levski',
        'sport': 'football',
        'information': 'Great club!',
        'picture': 'https://some-pic.png'
    }

    @staticmethod
    def __create_club(**credentials):
        return Club.objects.create(**credentials)

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

    def __get_response_for_club(self, club):
        return self.client.get(reverse('club info', kwargs={'pk': club.pk}))

    def __create_player_for_user(self, user):
        player = Player.objects.create(
            **self.VALID_PLAYER_DATA,
            user=user,
        )
        player.save()

        return player

    def test_club_details__expect_success(self):
        _, profile = self.__create_valid_user_and_profile()
        club = self.__create_club(**self.VALID_CLUB_DATA)

        response = self.__get_response_for_club(club)
        actual_club = response.context['object']

        self.assertEqual(club, actual_club)

    def test_club_details_expect_correct_template(self):
        _, profile = self.__create_valid_user_and_profile()
        club = self.__create_club(**self.VALID_CLUB_DATA)

        self.__get_response_for_club(club)

        self.assertTemplateUsed('web/club_details.html')
