from django.db import models

from .core import CoreModel
from .disease_category import DiseaseCategory


class Disease(CoreModel):
    name = models.CharField()
    display_name = models.CharField()
    description = models.CharField()
    category = models.ForeignKey(DiseaseCategory, on_delete=models.DO_NOTHING)

    class Meta:
        abstract = False

    def __str__(self):
        return self.name
