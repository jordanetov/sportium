# Generated by Django 4.0.3 on 2022-04-06 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='message',
            field=models.TextField(max_length=300),
        ),
    ]
