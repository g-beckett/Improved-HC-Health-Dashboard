from django.db import models
from django.urls import reverse
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

    def get_absolute_url(self):
        return reverse("dataportal:disease-detail", args=(self.pk, ))


class DiseaseTable(tables.Table):
    name = tables.Column(linkify=True)
    category = tables.Column(linkify=True)

    class Meta:
        model = Disease
        exclude = ('id', )
        sequence = ('name', 'category', 'description')

