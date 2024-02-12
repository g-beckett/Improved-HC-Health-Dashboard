from django.db import models

from .core import CoreModel


class DiseaseCategory(CoreModel):
    name = models.CharField()
    display_name = models.CharField()
    description = models.CharField()

    class Meta:
        abstract = False

    def __str__(self):
        return self.name
