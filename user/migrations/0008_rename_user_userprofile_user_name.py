# Generated by Django 5.0.6 on 2024-06-13 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_watchlistitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='user_name',
        ),
    ]