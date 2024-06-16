# Generated by Django 5.0.4 on 2024-06-16 10:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bids', '0001_initial'),
        ('vehicles', '0010_vehicle_seller'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='bid_amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='bid',
            old_name='created_at',
            new_name='timestamp',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='bidder',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='car',
        ),
        migrations.AddField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bid',
            name='vehicle',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle'),
            preserve_default=False,
        ),
    ]
