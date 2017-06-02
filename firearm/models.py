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
    serial_number = models.IntegerField(unique=True)
    restricted = models.BooleanField(default=True)
    type = models.IntegerField(choices=enumerate(TYPES))
    charge = models.IntegerField(choices=enumerate(CHARGES))
    calibre = models.DecimalField(decimal_places=3, max_digits=5
                                  )
