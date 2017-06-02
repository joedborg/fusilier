# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 15:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('town_of_birth', models.CharField(max_length=30)),
                ('address_first_line', models.CharField(max_length=30)),
                ('address_second_line', models.CharField(max_length=30)),
                ('address_town', models.CharField(max_length=30)),
                ('address_postcode', models.CharField(max_length=7)),
                ('phone_number', models.IntegerField()),
                ('photo', models.ImageField(upload_to='')),
                ('is_provisional', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
