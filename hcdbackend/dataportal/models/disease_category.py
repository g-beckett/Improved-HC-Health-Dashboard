from django.db import models
from django.urls import reverse
import django_tables2 as tables
from django_tables2.utils import A

from .base import BaseModel


class DiseaseCategory(BaseModel):
    name = models.CharField()
    description = models.TextField()

    class Meta:
        abstract = False

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("dataportal:disease-category-detail", args=(self.pk, ))

    def to_json(self):
        return {"name": self.name, "description": self.description}


class DiseaseCategoryTable(tables.Table):
    name = tables.Column(linkify=True)

    class Meta:
        model = DiseaseCategory
        exclude = ('id', )
        sequence = ('name', 'description')

