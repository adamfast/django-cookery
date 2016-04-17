# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookery', '0008_recipe_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='serves',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='serves how many people'),
        ),
    ]
