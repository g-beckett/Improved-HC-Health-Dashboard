from django.db import models

"""
BaseModel
"""


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True
