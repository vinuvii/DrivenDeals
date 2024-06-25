# Generated by Django 5.0.6 on 2024-06-24 12:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0015_payment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='body_type',
            field=models.CharField(choices=[('motorbike', 'Motorbike'), ('car', 'Car'), ('three_wheeler', 'Three Wheeler'), ('bicycle', 'Bicycle'), ('lorry', 'Lorry'), ('truck', 'Truck'), ('van', 'Van'), ('bus', 'Bus'), ('coupe', 'Coupe'), ('suv', 'SUV (Sport Utility Vehicle)'), ('tractor', 'Tractor'), ('atv', 'ATV (All-Terrain Vehicle)'), ('sedan', 'Sedan'), ('limousine', 'Limousine'), ('electric_vehicle', 'Electric Vehicle'), ('hybrid_vehicle', 'Hybrid Vehicle'), ('offroad_vehicle', 'Off-Road Vehicle'), ('other', 'Other')], max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]