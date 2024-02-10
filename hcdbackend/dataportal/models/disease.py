from django.db import models

from .disease_category import DiseaseCategory


class Disease(models.Model):
    name = models.CharField()
    description = models.CharField()
    category = models.ForeignKey(DiseaseCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
