# Generated by Django 4.0.3 on 2022-04-14 17:55

import django.core.validators
from django.db import migrations, models
import sportium.common.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_contacts_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('Game', 'Game'), ('Celebration', 'Celebration'), ('Tournament', 'Tournament'), ('Meet the team', 'Meet the team')], max_length=13)),
                ('day_and_time', models.CharField(choices=[('Monday at 19:00', 'Monday at 19:00'), ('Wednesday at 12:00', 'Wednesday at 12:00'), ('Wednesday at 19:00', 'Wednesday at 19:00'), ('Friday at 19:00', 'Friday at 19:00'), ('Saturday at 10:00', 'Saturday at 10:00'), ('Saturday ay 20:00', 'Saturday ay 20:00'), ('Sunday at 20:00', 'Sunday at 20:00')], max_length=18)),
                ('location', models.CharField(choices=[('Arena Sportium', 'Arena Sportium'), ('Ceremony hall - Arena Sportium', 'Ceremony hall - Arena Sportium'), ('The garden next to Sportium Stadium', 'The garden next to Sportium Stadium'), ('Sportium Stadium', 'Sportium Stadium'), ('Tennis club Sportium', 'Tennis club Sportium'), ('Swimming pool Sportium', 'Swimming pool Sportium')], max_length=35)),
                ('information', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='player',
            name='first_name',
            field=models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(1), sportium.common.validators.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='player',
            name='last_name',
            field=models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(1), sportium.common.validators.validate_only_letters]),
        ),
    ]
