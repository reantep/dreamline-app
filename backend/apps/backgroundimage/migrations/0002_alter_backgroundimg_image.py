# Generated by Django 3.2.4 on 2021-11-24 22:29

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backgroundimage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backgroundimg',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]