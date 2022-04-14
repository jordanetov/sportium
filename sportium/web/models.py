from datetime import datetime

from django.core.validators import MinLengthValidator
from django.db import models

from sportium.common.helpers import UserModel
from sportium.common.validators import validate_only_letters


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
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters,
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


class Contacts(models.Model):
    NAME_MAX_LEN = 16
    MESSAGE_MAX_LEN = 300

    name = models.CharField(
        max_length=NAME_MAX_LEN,
    )

    email = models.EmailField()

    message = models.TextField(
        max_length=MESSAGE_MAX_LEN,
    )

    def __str__(self):
        return f'{self.name}'


class Event(models.Model):
    NAME_MAX_LEN = 30

    GAME = 'Game'
    CELEBRATION = 'Celebration'
    TOURNAMENT = 'Tournament'
    MEETING = 'Meet the team'

    SPORTS_HALL = 'Arena Sportium'
    CEREMONY_HALL = 'Ceremony hall - Arena Sportium'
    GARDEN = 'The garden next to Sportium Stadium'
    STADIUM = 'Sportium Stadium'
    TENNIS_CLUB = 'Tennis club Sportium'
    SWIMMING_POOL = 'Swimming pool Sportium'

    MONDAY_EVENING = 'Monday at 19:00'
    WEDNESDAY_NOON = 'Wednesday at 12:00'
    WEDNESDAY_EVENING = 'Wednesday at 19:00'
    FRIDAY_EVENING = 'Friday at 19:00'
    WEEKEND_MORNING = 'Saturday at 10:00'
    SATURDAY_GAME = 'Saturday at 20:00'
    SUNDAY_GAME = 'Sunday at 20:00'

    EVENT_TYPES = [(t, t) for t in (GAME, CELEBRATION, TOURNAMENT, MEETING)]
    LOCATIONS = [(l, l) for l in (SPORTS_HALL, CEREMONY_HALL, GARDEN, STADIUM, TENNIS_CLUB, SWIMMING_POOL)]
    DAY_TIME_OPTIONS = [(o, o) for o in (
        MONDAY_EVENING, WEDNESDAY_NOON, WEDNESDAY_EVENING, FRIDAY_EVENING, WEEKEND_MORNING, SATURDAY_GAME, SUNDAY_GAME)]

    name = models.CharField(
        max_length=NAME_MAX_LEN,
    )

    type = models.CharField(
        max_length=max(len(t) for t, _ in EVENT_TYPES),
        choices=EVENT_TYPES,
    )

    day_and_time = models.CharField(
        max_length=max(len(o) for o, _ in DAY_TIME_OPTIONS),
        choices=DAY_TIME_OPTIONS,
    )

    location = models.CharField(
        max_length=max(len(l) for l, _ in LOCATIONS),
        choices=LOCATIONS,
    )

    information = models.TextField()

    def __str__(self):
        return f'{self.name}'
