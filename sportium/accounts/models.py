from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

from sportium.accounts.managers import SportiumUserManager


class SportiumUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LEN = 19

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = SportiumUserManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 16
    FIRST_NAME_MIN_LENGTH = 1
    LAST_NAME_MAX_LENGTH = 16
    LAST_NAME_MIN_LENGTH = 1

    MALE = "Male"
    FEMALE = "Female"
    NON_BINARY = "Non-Binary"
    PREFER_NOT_TO_SAY = "Prefer not to say"

    GENDERS = [(x, x) for x in (MALE, FEMALE, NON_BINARY, PREFER_NOT_TO_SAY)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            # todo: validate only letters
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            # todo: validate only letters
        )
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    personal_information = models.TextField(
        null=True,
        blank=True,
    )

    picture = models.URLField()

    email = models.EmailField(
        # null=True,
        # blank=True,
    )

    gender = models.CharField(
        max_length=max(len(g) for g, _ in GENDERS),
        choices=GENDERS,
    )

    user = models.OneToOneField(
        SportiumUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
