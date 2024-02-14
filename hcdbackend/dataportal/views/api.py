import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.core import serializers

from dataportal.models import DiseaseCategory, Disease, CaseReport

"""
Right now this will just return everything all once. Will want to clean up + make queryable, but should work to get
started with.

TODO: This in-box serialize works, but it will probably be better to write them out custom for each model so
that the response format is cleaner.

Will build off this single endpoint + POST data providing the query.
"""


def data_portal_api(request):

    if request.method not in ['GET', 'POST']:
        return HttpResponseBadRequest("API Request Method must be GET/POST")

    disease_categories = json.loads(serializers.serialize("json", DiseaseCategory.objects.all()))
    disease = json.loads(serializers.serialize("json", Disease.objects.all()))
    case_reports = json.loads(serializers.serialize("json", CaseReport.objects.all()))

    res = {"disease_categories": disease_categories,
           "disease": disease,
           "case_reports": case_reports}

    return JsonResponse(res)
