# Generated by Django 5.0.4 on 2024-06-19 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0011_alter_vehicle_engine_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='auction_duration_days',
            field=models.PositiveIntegerField(default=7),
        ),
    ]