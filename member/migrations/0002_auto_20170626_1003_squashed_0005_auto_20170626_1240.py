g# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-26 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    replaces = [('member', '0002_auto_20170626_1003'), ('member', '0003_auto_20170626_1010'), ('member', '0004_member_address_county'), ('member', '0005_auto_20170626_1240')]

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='membership_number',
            field=models.CharField(max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='member',
            name='country_of_birth',
            field=models.CharField(max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='address_first_line',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='address_postcode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='member',
            name='address_second_line',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='address_town',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128),
        ),
        migrations.AlterField(
            model_name='member',
            name='town_of_birth',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='member',
            name='address_county',
            field=models.CharField(max_length=50),
            preserve_default=False,
        ),
    ]