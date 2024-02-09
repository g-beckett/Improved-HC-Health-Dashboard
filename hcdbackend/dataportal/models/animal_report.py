from django.db import models

from .animal import Animal
from .area import Area


class AnimalReport(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    date = models.DateField()
