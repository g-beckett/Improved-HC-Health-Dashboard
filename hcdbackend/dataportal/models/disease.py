from django.db import models
import django_tables2 as tables

from .base import BaseModel
from .disease_category import DiseaseCategory


class Disease(BaseModel):
    name = models.CharField()
    description = models.TextField()
    category = models.ForeignKey(DiseaseCategory, on_delete=models.CASCADE)

    class Meta:
        abstract = False

    def __str__(self):
        return self.name


class DiseaseTable(tables.Table):
    class Meta:
        model = Disease
