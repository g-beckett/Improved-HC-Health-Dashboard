from django.db import models
import django_tables2 as tables

from .base import BaseModel


class DiseaseCategory(BaseModel):
    name = models.CharField()
    description = models.TextField()

    class Meta:
        abstract = False

    def __str__(self):
        return self.name


class DiseaseCategoryTable(tables.Table):
    class Meta:
        model = DiseaseCategory
