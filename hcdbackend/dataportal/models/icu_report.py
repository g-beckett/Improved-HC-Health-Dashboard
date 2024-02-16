from django.db import models
from django.urls import reverse
import django_tables2 as tables

from .base import BaseModel
from .disease import Disease


class ICUReport(BaseModel):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    icu_count = models.IntegerField()
    report_start_date = models.DateField()
    report_end_date = models.DateField()
    report_submission_date = models.DateField()

    class Meta:
        abstract = False

    def get_absolute_url(self):
        return reverse("dataportal:icu-report-detail", args=(self.pk, ))


class ICUReportTable(tables.Table):
    id = tables.Column(linkify=True)
    disease = tables.Column(linkify=True)
    category = tables.Column(linkify=True, accessor='disease.category')

    class Meta:
        model = ICUReport
        sequence = ('id', 'disease', 'category', 'report_submission_date', 'report_start_date', 'report_end_date')
