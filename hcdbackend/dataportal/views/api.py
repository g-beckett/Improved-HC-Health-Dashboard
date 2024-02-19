import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.core import serializers

from dataportal.models import DiseaseCategory, Disease, CaseReport, HospitalizedReport, ICUReport, DeathReport
from dataportal.models import VaccinationReport

"""
Right now this will just return everything all once. Will want to clean up + make queryable, but should work to get
started with.

URL Query Params. Use These.
Mock Data Generation Script.
CSS/Content Improvements.
Start looking at authentication.
https://docs.djangoproject.com/en/5.0/topics/auth/


Will build off this single endpoint + POST data or URL Args providing the query.
"""


def data_portal_api(request):
    """
    Note: Doing joins on disease/disease_category for each item in each report was slow, this speeds things up even
    though it looks hacky. There is probably a better way.
    """

    if request.method not in ['GET']:
        return HttpResponseBadRequest("API Request Method must be GET")

    disease_category_objs = DiseaseCategory.objects.all()
    disease_categories_json = [v.to_json() for v in DiseaseCategory.objects.all()]
    diseases_json = []
    case_reports_json = []
    hospitalized_reports_json = []
    icu_reports_json = []
    death_reports_json = []
    vaccination_reports_json = []

    for d_c in disease_category_objs:

        disease_objs = Disease.objects.filter(category=d_c)
        d_c_name = d_c.name

        for d in disease_objs:

            diseases_json.append(d.to_json())
            d_name = d.name

            case_reports = CaseReport.objects.filter(disease=d)
            for v in case_reports:
                v = v.to_json()
                v['Disease'] = d_name
                v['DiseaseCategory'] = d_c_name
                case_reports_json.append(v)

            hospitalized_reports = HospitalizedReport.objects.filter(disease=d)
            for v in hospitalized_reports:
                v = v.to_json()
                v['Disease'] = d_name
                v['DiseaseCategory'] = d_c_name
                hospitalized_reports_json.append(v)

            icu_reports = ICUReport.objects.filter(disease=d)
            for v in icu_reports:
                v = v.to_json()
                v['Disease'] = d_name
                v['DiseaseCategory'] = d_c_name
                icu_reports_json.append(v)

            death_reports = DeathReport.objects.filter(disease=d)
            for v in death_reports:
                v = v.to_json()
                v['Disease'] = d_name
                v['DiseaseCategory'] = d_c_name
                death_reports_json.append(v)

            vaccination_reports = VaccinationReport.objects.filter(disease=d)
            for v in vaccination_reports:
                v = v.to_json()
                v['Disease'] = d_name
                v['DiseaseCategory'] = d_c_name
                vaccination_reports_json.append(v)

    res = {"DiseaseCategories": disease_categories_json,
           "Diseases": diseases_json,
           "CaseReports": case_reports_json,
           "HospitalizedReports": hospitalized_reports_json,
           "ICUReports": icu_reports_json,
           "DeathReports": death_reports_json,
           "VaccinationReports": vaccination_reports_json}

    return JsonResponse(res)
