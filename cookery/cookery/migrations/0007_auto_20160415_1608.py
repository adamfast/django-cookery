# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 21:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cookery', '0006_auto_20160414_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='MealTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True, verbose_name='Name')),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='meal',
            field=models.ForeignKey(blank=True, help_text='Meal', on_delete=django.db.models.deletion.CASCADE, to='cookery.MealTime'),
        ),
        migrations.AddField(
            model_name='meal',
            name='recipes',
            field=models.ManyToManyField(to='cookery.Recipe'),
        ),
    ]
