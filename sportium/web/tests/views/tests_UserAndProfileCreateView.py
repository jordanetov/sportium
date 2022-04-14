from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from sportium.accounts.models import Profile

UserModel = get_user_model()


class ProfileCreateViewTests(TestCase):
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

    def test_create_user_and_profile__when_all_valid__expect_to_create(self):
        self.client.post(
            reverse('register'),
            data=self.VALID_PROFILE_DATA,
        )

        user, profile = self.__create_valid_user_and_profile()

        self.assertIsNotNone(profile)
        self.assertEqual(self.VALID_PROFILE_DATA['first_name'], profile.first_name)
        self.assertEqual(self.VALID_PROFILE_DATA['last_name'], profile.last_name)
        self.assertEqual(self.VALID_PROFILE_DATA['date_of_birth'], profile.date_of_birth)
        self.assertEqual(self.VALID_PROFILE_DATA['personal_information'], profile.personal_information)
        self.assertEqual(self.VALID_PROFILE_DATA['picture'], profile.picture)
        self.assertEqual(self.VALID_PROFILE_DATA['email'], profile.email)
        self.assertEqual(self.VALID_PROFILE_DATA['gender'], profile.gender)

    def test_create_profile__when_all_valid__expect_to_redirect_to_home(self):
        response = self.client.post(
            reverse('register'),
            data=self.VALID_PROFILE_DATA,
        )

        user, profile = self.__create_valid_user_and_profile()

        self.assertIsNotNone(profile)
        self.assertEqual(response.status_code, 200)

    def test_create_profile_when_profile_with_same_first_and_last_name_exists__expect_error(self):
        user, profile = self.__create_valid_user_and_profile()

        self.client.post(
            reverse('register'),
            data=self.VALID_PROFILE_DATA,
        )

        profiles = Profile.objects.filter(**self.VALID_PROFILE_DATA)

        self.assertEqual(1, len(profiles))
