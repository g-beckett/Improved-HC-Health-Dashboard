from django.db import models

"""
CoreModel
"""


class CoreModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True
