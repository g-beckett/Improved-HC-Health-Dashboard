from django.db import models


"""
BaseModel

All other models inherit from this one.
"""


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True
