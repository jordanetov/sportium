from django.core.validators import MinLengthValidator
from django.db import models

from sportium.common.helpers import UserModel


class Club(models.Model):
    NAME_MAX_LEN = 16
    NAME_MIN_LEN = 2

    FOOTBALL = "Football"
    VOLLEYBALL = "Volleyball"
    TENNIS = "Tennis"
    SWIMMING = "Swimming"
    ATHLETICS = "Athletics"

    SPORTS = [(s, s) for s in (FOOTBALL, VOLLEYBALL, TENNIS, SWIMMING, ATHLETICS)]

    name = models.CharField(
        unique=True,
        max_length=NAME_MAX_LEN,
        validators=(
            MinLengthValidator(NAME_MIN_LEN),
        )
    )

    sport = models.CharField(
        max_length=max(len(s) for s, _ in SPORTS),
        choices=SPORTS,
    )

    information = models.TextField()

    picture = models.ImageField()

    def __str__(self):
        return f'{self.name}'


class Player(models.Model):
    FIRST_NAME_MAX_LEN = 16
    FIRST_NAME_MIN_LEN = 1
    LAST_NAME_MAX_LEN = 16
    LAST_NAME_MIN_LEN = 1

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
        )
    )

    date_of_birth = models.DateField()

    picture = models.URLField(
        null=True,
        blank=True,
    )

    clubs = models.ManyToManyField(
        Club,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    date_time_of_joining = models.DateTimeField(
        auto_now_add=True,
    )

    @property
    def age(self):
        import datetime
        d_o_b = self.date_of_birth
        current_date_info = datetime.date.today()
        my_age = (current_date_info.year - d_o_b.year) - int(
            (current_date_info.month, current_date_info.day) < (d_o_b.month, d_o_b.day)
        )
        return my_age

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
