# Generated by Django 5.0.6 on 2024-06-24 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0017_testimonial_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmessage',
            old_name='message',
            new_name='review',
        ),
        migrations.DeleteModel(
            name='Testimonial',
        ),
    ]
