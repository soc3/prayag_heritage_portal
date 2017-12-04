# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TourismPlaces', '0002_tourismplace_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourismplace',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_for', to='TourismPlaces.Image'),
        ),
        migrations.AlterField(
            model_name='image',
            name='tourism_place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TourismPlace_for', to='TourismPlaces.TourismPlace'),
        ),
    ]