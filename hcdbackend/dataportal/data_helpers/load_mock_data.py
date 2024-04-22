import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hcdbackend.settings")

import django
django.setup()

from dataportal.models import Disease, CaseReport, HospitalizedReport, DeathReport

"""
Script for loading mock data.

Will use JSON files present in the /mock_data folder. See mock_data_gen_2.py to generate those.

NOTE: This is setup to do full imports. Existing reports will be deleted/re-imported
from the JSON data in /mock_data. This is to avoid double imports.
"""


def load_json(file_path: str):

    with open(file_path, "r") as r_file:
        return json.load(r_file)


def load_mock_data_report(mock_data_fn: str):

    mock_data = load_json(f"mock_data/{mock_data_fn}")
    disease_name = mock_data['case_reports'][0]['disease']
    if disease_name == "HIV-AIDS":
        disease_name = "HIV/AIDS"

    # Get Existing Disease Obj
    disease_obj = Disease.objects.get(name=disease_name)

    # Clear Existing Reports
    existing_case_reports = CaseReport.objects.filter(disease=disease_obj)
    existing_case_reports.delete()

    existing_death_reports = DeathReport.objects.filter(disease=disease_obj)
    existing_death_reports.delete()

    existing_hospitalized_reports = HospitalizedReport.objects.filter(disease=disease_obj)
    existing_hospitalized_reports.delete()

    # Load New Reports
    for v in mock_data['case_reports']:
        v['disease'] = disease_obj
        new_case_report = CaseReport(**v)
        new_case_report.save()

    for v in mock_data['death_reports']:
        v['disease'] = disease_obj
        new_death_report = DeathReport(**v)
        new_death_report.save()

    for v in mock_data['hospitalized_reports']:
        v['disease'] = disease_obj
        new_hospitalized_report = HospitalizedReport(**v)
        new_hospitalized_report.save()

    print("OK", disease_name)


def main():

    # Commented out for safety, but run this to refresh the status report data
    for v in os.listdir("mock_data"):

        # if v not in ['Campylobacter_mock.json']:
        #     continue

        load_mock_data_report(v)


if __name__ == "__main__":

    main()


