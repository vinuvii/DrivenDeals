# Generated by Django 5.0.6 on 2024-06-11 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email_address',
        ),
    ]