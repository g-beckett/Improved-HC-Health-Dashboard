from django.db import models

from .species import Species


class Animal(models.Model):
    name = models.CharField(max_length=50)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
