# Generated by Django 4.0.3 on 2022-04-03 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_player_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='picture',
            field=models.URLField(blank=True, null=True),
        ),
    ]
