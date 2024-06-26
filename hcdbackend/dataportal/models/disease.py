from django.db import models
from django.urls import reverse
import django_tables2 as tables

from .base import BaseModel
from .disease_category import DiseaseCategory


"""
Disease represents a particular disease in the real-world. Each disease belong to a single disease category.

All reports are tied to a single disease.

Some educational information + descriptions are present for potential use by the dashboard independent of the reports.
"""


class Disease(BaseModel):
    name = models.CharField()
    description = models.TextField()
    cdc_link = models.TextField(default="Link Me")
    wiki_link = models.TextField(default="Link Me")
    mayo_link = models.TextField(default="Link Me")
    category = models.ForeignKey(DiseaseCategory, on_delete=models.CASCADE)

    class Meta:
        abstract = False

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("dataportal:disease-detail", args=(self.pk, ))

    def to_json(self):
        return {"name": self.name, "description": self.description, "diseaseCategory": self.category.name,
                "cdc_link": self.cdc_link, "wiki_link": self.wiki_link, "mayo_link": self.mayo_link}


class DiseaseTable(tables.Table):
    name = tables.Column(linkify=True)
    category = tables.Column(linkify=True)

    class Meta:
        model = Disease
        exclude = ('id', 'cdc_link', 'wiki_link', 'mayo_link',)
        sequence = ('name', 'category', 'description')

