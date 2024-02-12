from django.db import models

from .core import CoreModel
from .disease_category import DiseaseCategory


class Disease(CoreModel):
    name = models.CharField(primary_key=True)
    display_name = models.CharField()
    description = models.CharField()
    category = models.ForeignKey(DiseaseCategory, on_delete=models.CASCADE)

    class Meta:
        abstract = False

    def __str__(self):
        return self.name
