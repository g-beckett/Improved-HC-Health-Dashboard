import json
from datetime import datetime, timedelta
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hcdbackend.settings")

import django
django.setup()

from dataportal.models import Disease, CaseReport, HospitalizedReport, DeathReport

"""
DEPRECATED - See load_mock_data.py

Keeping this script around though for context, but do not use.

Script for initial data loading for COVID-19.

NOTE: This is setup to do full imports on COVID-19 Data. Existing COVID-19 reports will be deleted/re-imported
from the JSON data in /case_data. This is to avoid double imports.
"""


def load_json(file_path: str):

    with open(file_path, "r") as r_file:
        return json.load(r_file)


def load_case_reports():
    """
    Fields for CaseReport. For now we'll just populate case_count and the dates.

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
    report_start_date = models.DateField()
    report_end_date = models.DateField()
    report_submission_date = models.DateField()
    """

    covid_19_obj = Disease.objects.get(name='COVID-19')

    existing_reports = CaseReport.objects.filter(disease=covid_19_obj)
    existing_reports.delete()

    report_data = load_json(file_path="case_data/NewCases_data.json")
    report_data = report_data['d']

    print(f"Importing: {len(report_data)} CaseReports")
    for i, v in enumerate(report_data):
        case_count = int(v['NumberOfNewCases'])
        case_date = v['AnalyticsDate']
        case_date = datetime.strptime(case_date, '%m/%d/%Y')
        case_date = case_date.strftime("%Y-%m-%d")
        submit_date = datetime.now().strftime("%Y-%m-%d")

        new_case_report = CaseReport(disease=covid_19_obj, report_start_date=case_date, report_end_date=case_date,
                                     report_submission_date=submit_date, case_count=case_count)
        new_case_report.save()
        if i % 10 == 0:
            print(i, new_case_report.id)


def load_hospitalized_reports():
    """
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    inpatient_count = models.IntegerField()
    under_investigation_count = models.IntegerField()
    report_start_date = models.DateField()
    report_end_date = models.DateField()
    report_submission_date = models.DateField()
    """

    covid_19_obj = Disease.objects.get(name='COVID-19')

    existing_reports = HospitalizedReport.objects.filter(disease=covid_19_obj)
    existing_reports.delete()

    report_data = load_json(file_path="case_data/InpatientsAndPUIs_data.json")
    report_data = report_data['d']

    print(f"Importing: {len(report_data)} HospitalizedReports")
    for i, v in enumerate(report_data):
        inpatient_count = int(v['HospitalizedInpatientsInHamiltonCounty'])
        under_investigation_count = int(v['HospitalizedPeopleUnderInvestigationInHamiltonCounty'])
        report_date = v['AnalyticsDate']
        report_date = datetime.strptime(report_date, '%m/%d/%Y')
        report_date = report_date.strftime("%Y-%m-%d")
        submit_date = datetime.now().strftime("%Y-%m-%d")

        new_report = HospitalizedReport(disease=covid_19_obj, report_start_date=report_date, report_end_date=report_date,
                                        report_submission_date=submit_date, inpatient_count=inpatient_count,
                                        under_investigation_count=under_investigation_count)
        new_report.save()
        if i % 10 == 0:
            print(i, new_report.id)


def load_death_reports():
    """
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    death_count = models.IntegerField()
    report_start_date = models.DateField()
    report_end_date = models.DateField()
    report_submission_date = models.DateField()
    """

    covid_19_obj = Disease.objects.get(name='COVID-19')

    existing_reports = DeathReport.objects.filter(disease=covid_19_obj)
    existing_reports.delete()

    report_data = load_json(file_path="case_data/Deaths_data.json")
    report_data = report_data['d']

    print(f"Importing: {len(report_data)} DeathReports")
    for i, v in enumerate(report_data):
        try:
            death_count = int(v['Deaths'])
        except ValueError:
            death_count = 0
        report_date = v['AnalyticsDate']
        report_date = datetime.strptime(report_date, '%m/%d/%Y')
        report_start_date = report_date + timedelta(days=-6)
        report_date = report_date.strftime("%Y-%m-%d")
        report_start_date = report_start_date.strftime("%Y-%m-%d")
        submit_date = datetime.now().strftime("%Y-%m-%d")

        new_report = DeathReport(disease=covid_19_obj, report_start_date=report_start_date,
                                 report_end_date=report_date,
                                 report_submission_date=submit_date, death_count=death_count)
        new_report.save()
        if i % 10 == 0:
            print(i, new_report.id)


if __name__ == "__main__":

    # load_case_reports()
    # load_hospitalized_reports()
    # load_death_reports()

    pass

