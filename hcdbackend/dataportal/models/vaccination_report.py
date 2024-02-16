from django.db import models
from django.urls import reverse
import django_tables2 as tables
from datetime import datetime

from .base import BaseModel
from .disease import Disease


class VaccinationReport(BaseModel):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    vaccination_count = models.IntegerField()
    report_start_date = models.DateField()
    report_end_date = models.DateField()
    report_submission_date = models.DateField()

    class Meta:
        abstract = False

    def get_absolute_url(self):
        return reverse("dataportal:vaccination-report-detail", args=(self.pk, ))

    def to_json(self):
        analytics_date = str(self.report_end_date)
        analytics_date = datetime.strptime(analytics_date, '%Y-%m-%d')
        analytics_date = analytics_date.strftime('%m/%d/%Y') + ' 12:00:00 AM'
        return {"AnalyticsRecordID": self.pk, "VaccinationCount": self.vaccination_count,
                "AnalyticsDate": analytics_date}


class VaccinationReportTable(tables.Table):
    id = tables.Column(linkify=True)
    disease = tables.Column(linkify=True)
    category = tables.Column(linkify=True, accessor='disease.category')

    class Meta:
        model = VaccinationReport
        sequence = ('id', 'disease', 'category', 'report_submission_date', 'report_start_date', 'report_end_date')
        order_by = ('-report_start_date',)