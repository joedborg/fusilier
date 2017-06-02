from django.db import models
from firearm.models import Firearm
from member.models import Member


RANGES = [
    'Bicester',
    'Chesterton'
]

SESSIONS = [
    'Practice',
    'Competition'
]


class Visit(models.Model):
    member = models.ForeignKey(Member)
    range = models.IntegerField(choices=enumerate(RANGES))
    timestamp = models.DateTimeField(auto_now=True)
    firearm = models.ForeignKey(Firearm)
    session = models.IntegerField(choices=enumerate(SESSIONS))

    def __str__(self):
        return '%s on %s in %s' % (self.member, self.timestamp, self.range)
