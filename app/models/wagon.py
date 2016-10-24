from django.db import models

from .train import Train
from .service import Service


class WagonServiceClass(models.Model):
    """
    Классы обслуживания - 1А, ЗП, 1/1 и т.д.
    """
    name = models.CharField(max_length=5)
    description = models.TextField()

    def __str__(self):
        return '{} ({})'.format(self.name, self.description)


class WagonType(models.Model):
    # name - Люкс, СВ, Купейный и т.д.
    name = models.CharField(max_length=50)
    service_class = models.ForeignKey(
        to=WagonServiceClass,
        related_name='wagon_types',
    )

    def __str__(self):
        return self.name


class WagonCategory(models.Model):
    """
    Категории вагонов - Б - бизнес класс, Ж - возможна перевозка
    домашних животных и т.д.
    """
    name = models.CharField(max_length=5)
    description = models.TextField()

    def __str__(self):
        return '{} ({})'.format(self.name, self.description)


class Wagon(models.Model):
    number = models.PositiveSmallIntegerField()
    train = models.ForeignKey(to=Train, related_name='wagons')
    type = models.ForeignKey(to=WagonType, related_name='wagons')
    category = models.ForeignKey(to=WagonCategory, related_name='wagons')
    services = models.ManyToManyField(to=Service, related_name='wagon_types')

    def __str__(self):
        return '{} - {}'.format(self.number, self.train)


class WagonPlace(models.Model):
    number = models.PositiveSmallIntegerField()
    # True - нижнее, False - верхнее
    is_below = models.BooleanField()
    is_free = models.BooleanField()
    is_for_animals = models.BooleanField()
    # Место матери и ребёнка
    is_mother_baby = models.BooleanField()
    wagon = models.ForeignKey(to=Wagon, related_name='scheme')

    def __str__(self):
        return '{} - {}'.format(self.number, self.wagon)
