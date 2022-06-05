# Generated by Django 4.0.4 on 2022-06-04 11:19

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_auto_20220601_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='imageURL',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Image'),
        ),
    ]
