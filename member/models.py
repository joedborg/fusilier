from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField()
    town_of_birth = models.CharField(max_length=30)
    address_first_line = models.CharField(max_length=30)
    address_second_line = models.CharField(max_length=30, blank=True, null=True)
    address_town = models.CharField(max_length=30)
    address_postcode = models.CharField(max_length=8)
    phone_number = models.IntegerField()
    photo = models.ImageField()
    is_provisional = models.BooleanField(default=True)
