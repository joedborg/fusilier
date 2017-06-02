from django.db import models
from member.models import Member


TYPES = [
    'Pistol',
    'Rifle'
]

CHARGES = [
    'Air',
    'Gunpowder',
    'Blackpowder'
]


class Firearm(models.Model):
    owner = models.ForeignKey(Member)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    serial_number = models.IntegerField(unique=True)
    restricted = models.BooleanField(default=True)
    type = models.IntegerField(choices=enumerate(TYPES))
    charge = models.IntegerField(choices=enumerate(CHARGES))
    calibre = models.DecimalField(decimal_places=3, max_digits=5)

    def __str__(self):
        return '%s %s' % (self.make, self.model)
