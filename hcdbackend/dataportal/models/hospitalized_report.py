from django.db import models
from django.urls import reverse
import django_tables2 as tables

from .base import BaseModel
from .disease import Disease


class HospitalizedReport(BaseModel):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    inpatient_count = models.IntegerField()
    under_investigation_count = models.IntegerField()
    report_start_date = models.DateField()
    report_end_date = models.DateField()
    report_submission_date = models.DateField()

    class Meta:
        abstract = False

    def get_absolute_url(self):
        return reverse("dataportal:hospitalized-report-detail", args=(self.pk, ))


class HospitalizedReportTable(tables.Table):
    id = tables.Column(linkify=True)
    disease = tables.Column(linkify=True)
    category = tables.Column(linkify=True, accessor='disease.category')

    class Meta:
        model = HospitalizedReport
        sequence = ('id', 'disease', 'category', 'report_submission_date', 'report_start_date', 'report_end_date')
