import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.core import serializers
from django.db import models

from dataportal.models import DiseaseCategory, Disease, CaseReport, HospitalizedReport, DeathReport

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
    death_reports_json = []

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

            death_reports = DeathReport.objects.filter(disease=d)
            for v in death_reports:
                v = v.to_json()
                v['Disease'] = d_name
                v['DiseaseCategory'] = d_c_name
                death_reports_json.append(v)

    res = {"DiseaseCategories": disease_categories_json,
           "Diseases": diseases_json,
           "CaseReports": case_reports_json,
           "HospitalizedReports": hospitalized_reports_json,
           "ICUReports": [],
           "DeathReports": death_reports_json,
           "VaccinationReports": []}

    return JsonResponse(res)

REPORT_TYPES = {"case_report": CaseReport, "death_report": DeathReport, 
                "hospitalized_report": HospitalizedReport}

FILTER_TYPES = {"disease_category": DiseaseCategory, "disease": Disease}


def data_portal_api2(request):

    if request.method not in ['GET']:
        return HttpResponseBadRequest("API Request Method must be GET")

    #req param takes in a string of words from the list the takes in user input, double check it is in the list
    #checks if any param is entered, if true, run x else: print all, 
    #verify if its valid, one you know each element is valid, then write the codde to fetch the correct reports

    report_queries = request.GET.getlist("healthcare_reports", None)
    filter_queries = request.GET.getlist("filter_reports", None)
    print(report_queries)

    if not report_queries:
        return getAllReports()
       
    return getSpecificReports(report_queries)            

#the getAllReports and getSpecificReports work fine but i don't think the fitler is
    # still working properly. I have still been trying to work on it though.
def getAllReports(filters = None):
    report_object_list = [report_object for report_object in REPORT_TYPES.values()]

    if filters:
        report_object_list = applyFilters(report_object_list, filters)

    report_json = [[entry.to_json() for entry in report_object.objects.all()] for report_object in report_object_list]
    return JsonResponse({"reports": report_json})

def getSpecificReports(report_queries, filters=None):
    for query in report_queries:
        if query not in REPORT_TYPES.keys():           
            return HttpResponseBadRequest("Please provide a valid report query parameters")
        #Salmonella
    if filters:
        report_object = applyFilters(report_object, filters)
      
    report_json = [[entry.to_json() for entry in REPORT_TYPES.get(query).objects.all()] for query in report_queries]
    return JsonResponse({"reports": report_json})

def applyFilters(report_object, filter_queries):
    for query in filter_queries:
        if query not in FILTER_TYPES.keys():
            return HttpResponseBadRequest("Please provide a valid filter query parameters")
        
       # filter_function = FILTER_TYPES[query]
        filter_json = [[entry.to_json() for entry in FILTER_TYPES.get(query).objects.all()] for query in filter_queries]
    return JsonResponse({"reports": filter_json})


# def applyFilters(filter_queries):
#     for query in filter_queries:
#         if query not in FILTER_TYPES.keys():
#             return HttpResponseBadRequest("Please provide a valid filter query parameters")
#     filtered_object = filter(applyFilters, FILTER_TYPES)
#     print(list(filtered_object)) 
