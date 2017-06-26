from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Member(models.Model):
    user = models.OneToOneField(User)
    membership_number = models.CharField(max_length=5, unique=True)
    birthday = models.DateField()
    town_of_birth = models.CharField(max_length=50)
    country_of_birth = models.CharField(max_length=50)
    address_first_line = models.CharField(max_length=50)
    address_second_line = models.CharField(max_length=50, blank=True, null=True)
    address_town = models.CharField(max_length=50)
    address_county = models.CharField(max_length=50)
    address_postcode = models.CharField(max_length=10)
    phone_number = PhoneNumberField()
    photo = models.ImageField(blank=True, null=True)
    is_provisional = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
