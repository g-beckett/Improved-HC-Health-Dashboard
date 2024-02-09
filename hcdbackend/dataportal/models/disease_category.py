from django.db import models


class DiseaseCategory(models.Model):
    name = models.CharField()
    description = models.CharField()

    def __str__(self):
        return self.name
