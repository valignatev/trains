from django.db import models

from .station import Station


class Route(models.Model):
    station = models.ForeignKey(Station, related_name='routes')
    arrival = models.DateTimeField()
    departure = models.DateTimeField()

    def __str__(self):
        return ','.join([str(self.station),
                         str(self.arrival),
                         str(self.departure)])
