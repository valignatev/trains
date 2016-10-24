from django.db import models
from django.contrib.auth.models import User

from .route import Route
from .train import Train
from .wagon import Wagon, WagonPlace


class Ticket(models.Model):
    origin = models.ForeignKey(to=Route, related_name='origin_tickets')
    destination = models.ForeignKey(to=Route, related_name='dest_tickets')
    train = models.ForeignKey(to=Train, related_name='tickets')
    wagon = models.ForeignKey(to=Wagon, related_name='tickets')
    # В общий вагон билет без места
    place = models.OneToOneField(
        to=WagonPlace,
        related_name='ticket',
        null=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(to=User, related_name='tickets')

