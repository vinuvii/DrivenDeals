# Generated by Django 5.0.4 on 2024-06-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0008_vehicle_abs_breaks_vehicle_air_conditioning_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='picture2',
            field=models.ImageField(blank=True, null=True, upload_to='vehicle_pictures/'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='picture3',
            field=models.ImageField(blank=True, null=True, upload_to='vehicle_pictures/'),
        ),
    ]