# Generated by Django 5.0.4 on 2024-06-19 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_watchlist_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userwatchlistitem',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='userwatchlistitem',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userwatchlistitem',
            name='vehicle',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.DeleteModel(
            name='UserWatchlistItem',
        ),
    ]
