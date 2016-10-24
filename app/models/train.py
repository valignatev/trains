from django.db import models

from .route import Route


class Train(models.Model):
    number = models.CharField(max_length=10)
    routes = models.ManyToManyField(Route, related_name='trains')

    def __str__(self):
        return self.number
