from django.db import models

from .base import BaseModel


class DiseaseCategory(BaseModel):
    name = models.CharField()
    description = models.TextField()

    class Meta:
        abstract = False

    def __str__(self):
        return self.name
