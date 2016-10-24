from django.db import models

from .service import Service


class Station(models.Model):
    name = models.CharField(max_length=100)
    # Services available on the station. Killer-feature of our application
    services = models.ManyToManyField(
        Service,
        related_name='stations',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
