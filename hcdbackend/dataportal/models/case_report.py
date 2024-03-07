from django.db import models
from django.urls import reverse
import django_tables2 as tables
from datetime import datetime

from .base import BaseModel
from .disease import Disease


class CaseReport(BaseModel):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    case_count = models.IntegerField(default=0)
    case_count_epi = models.IntegerField(default=0)
    sex_female_count = models.IntegerField(default=0)
    sex_male_count = models.IntegerField(default=0)
    sex_unknown_count = models.IntegerField(default=0)
    race_white_count = models.IntegerField(default=0)
    race_black_count = models.IntegerField(default=0)
    race_asian_count = models.IntegerField(default=0)
    race_native_american_count = models.IntegerField(default=0)
    race_other_count = models.IntegerField(default=0)
    race_unknown_count = models.IntegerField(default=0)
    ethnicity_hispanic_count = models.IntegerField(default=0)
    ethnicity_non_hispanic_count = models.IntegerField(default=0)
    ethnicity_unknown_count = models.IntegerField(default=0)
    age_0_10_count = models.IntegerField(default=0)
    age_11_20_count = models.IntegerField(default=0)
    age_21_30_count = models.IntegerField(default=0)
    age_31_40_count = models.IntegerField(default=0)
    age_41_50_count = models.IntegerField(default=0)
    age_51_60_count = models.IntegerField(default=0)
    age_61_70_count = models.IntegerField(default=0)
    age_71_80_count = models.IntegerField(default=0)
    age_81_and_up_count = models.IntegerField(default=0)
    age_unknown_count = models.IntegerField(default=0)
    sex_present = models.BooleanField(default=False)
    race_present = models.BooleanField(default=False)
    ethnicity_present = models.BooleanField(default=False)
    age_present = models.BooleanField(default=False)
    report_start_date = models.DateField()
    report_end_date = models.DateField()
    report_submission_date = models.DateField()


    class Meta:
        abstract = False

    def get_absolute_url(self):
        return reverse("dataportal:case-report-detail", args=(self.pk, ))

    def to_json(self):
        analytics_date = str(self.report_end_date)
        analytics_date = datetime.strptime(analytics_date, '%Y-%m-%d')
        analytics_date = analytics_date.strftime('%m/%d/%Y') + ' 12:00:00 AM'
        return {"AnalyticsRecordID": self.pk, "NumberOfNewCases": self.case_count, "AnalyticsDate": analytics_date}


class CaseReportTable(tables.Table):
    id = tables.Column(linkify=True)
    disease = tables.Column(linkify=True)
    category = tables.Column(linkify=True, accessor='disease.category')

    class Meta:
        model = CaseReport
        sequence = ('id', 'disease', 'category', 'report_submission_date', 'report_start_date', 'report_end_date')
        order_by = ('-report_start_date', )
