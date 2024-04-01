from django.http import JsonResponse, HttpResponseBadRequest

from dataportal.models import DiseaseCategory, Disease, CaseReport, HospitalizedReport, DeathReport

"""
These functions hold logic for our DataPortal's API and map to the /_query & /_query2 endpoints in views.py

data_portal_api_2() is the preferred method of access, which uses /_query2. Details of the URL Params are shown
in that functions comments.

URL Parameters are used to control behavior. Response is in JSON. Request Method is GET.
"""


def data_portal_api(request):
    """
    DEPRECATED - But still functional. See data_portal_api_2 below

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


def data_portal_api_2(request):
    """
    URL Params

    ?type: ['disease', 'disease_category', 'case_report', 'death_report', 'hospitalized_report'
    ?record_id: int
    ?disease: str
    ?disease_category: str

    Functionality
    GET ALL/1 Disease
    GET ALL/1 DiseaseCategory

    GET Reports By:
    1. ALL by type
    2. 1 by Record ID and type
    3. Filter By Disease and type
    4. Filer By Disease Category and type

    This is kinda messy but it works. Could probably be cleaned up, but these loops are to speed up the SQL query by
    not having to do joins.
    """

    if request.method not in ['GET']:
        return HttpResponseBadRequest("API Request Method must be GET")

    query_type = request.GET.get("type", None)
    record_id = request.GET.get("record_id", None)
    disease = request.GET.get("disease", None)
    disease_category = request.GET.get("disease_category", None)

    res = []

    match query_type:

        case "disease":

            if record_id:
                objs = Disease.objects.get(id=int(record_id))
                res = [objs.to_json()]
            else:
                objs = Disease.objects.all()
                res = [v.to_json() for v in objs]

        case "disease_category":

            if record_id:
                objs = DiseaseCategory.objects.get(id=int(record_id))
                res = [objs.to_json()]
            else:
                objs = DiseaseCategory.objects.all()
                res = [v.to_json() for v in objs]

        case "case_report":

            if record_id:
                obj = CaseReport.objects.get(id=int(record_id))

                d_name = obj.disease.name
                d_c_name = obj.disease.category.name

                res = [obj.to_json()]
                for v in res:
                    v['Disease'] = d_name
                    v['DiseaseCategory'] = d_c_name

            elif disease:
                disease_obj = Disease.objects.get(name=disease)
                objs = CaseReport.objects.filter(disease=disease_obj)

                d_name = disease_obj.name
                d_c_name = disease_obj.category.name

                res = [v.to_json() for v in objs]
                for v in res:
                    v['Disease'] = d_name
                    v['DiseaseCategory'] = d_c_name

            elif disease_category:
                disease_category_obj = DiseaseCategory.objects.get(name=disease_category)
                disease_objs = Disease.objects.filter(category=disease_category_obj)

                d_c_name = disease_category_obj.name
                res = []
                for d in disease_objs:
                    d_name = d.name
                    objs = CaseReport.objects.filter(disease=d)
                    for v in objs:
                        v = v.to_json()
                        v['Disease'] = d_name
                        v['DiseaseCategory'] = d_c_name
                        res.append(v)

            else:
                disease_category_objs = DiseaseCategory.objects.all()
                res = []
                for d_c in disease_category_objs:
                    disease_objs = Disease.objects.filter(category=d_c)
                    d_c_name = d_c.name
                    for d in disease_objs:
                        d_name = d.name
                        objs = CaseReport.objects.filter(disease=d)
                        for v in objs:
                            v = v.to_json()
                            v['Disease'] = d_name
                            v['DiseaseCategory'] = d_c_name
                            res.append(v)

        case "death_report":

            if record_id:
                obj = DeathReport.objects.get(id=int(record_id))

                d_name = obj.disease.name
                d_c_name = obj.disease.category.name

                res = [obj.to_json()]
                for v in res:
                    v['Disease'] = d_name
                    v['DiseaseCategory'] = d_c_name

            elif disease:
                disease_obj = Disease.objects.get(name=disease)
                objs = DeathReport.objects.filter(disease=disease_obj)

                d_name = disease_obj.name
                d_c_name = disease_obj.category.name

                res = [v.to_json() for v in objs]
                for v in res:
                    v['Disease'] = d_name
                    v['DiseaseCategory'] = d_c_name

            elif disease_category:
                disease_category_obj = DiseaseCategory.objects.get(name=disease_category)
                disease_objs = Disease.objects.filter(category=disease_category_obj)

                d_c_name = disease_category_obj.name
                res = []
                for d in disease_objs:
                    d_name = d.name
                    objs = DeathReport.objects.filter(disease=d)
                    for v in objs:
                        v = v.to_json()
                        v['Disease'] = d_name
                        v['DiseaseCategory'] = d_c_name
                        res.append(v)

            else:
                disease_category_objs = DiseaseCategory.objects.all()
                res = []
                for d_c in disease_category_objs:
                    disease_objs = Disease.objects.filter(category=d_c)
                    d_c_name = d_c.name
                    for d in disease_objs:
                        d_name = d.name
                        objs = DeathReport.objects.filter(disease=d)
                        for v in objs:
                            v = v.to_json()
                            v['Disease'] = d_name
                            v['DiseaseCategory'] = d_c_name
                            res.append(v)

        case "hospitalized_report":

            if record_id:
                obj = HospitalizedReport.objects.get(id=int(record_id))

                d_name = obj.disease.name
                d_c_name = obj.disease.category.name

                res = [obj.to_json()]
                for v in res:
                    v['Disease'] = d_name
                    v['DiseaseCategory'] = d_c_name

            elif disease:
                disease_obj = Disease.objects.get(name=disease)
                objs = HospitalizedReport.objects.filter(disease=disease_obj)

                d_name = disease_obj.name
                d_c_name = disease_obj.category.name

                res = [v.to_json() for v in objs]
                for v in res:
                    v['Disease'] = d_name
                    v['DiseaseCategory'] = d_c_name

            elif disease_category:
                disease_category_obj = DiseaseCategory.objects.get(name=disease_category)
                disease_objs = Disease.objects.filter(category=disease_category_obj)

                d_c_name = disease_category_obj.name
                res = []
                for d in disease_objs:
                    d_name = d.name
                    objs = HospitalizedReport.objects.filter(disease=d)
                    for v in objs:
                        v = v.to_json()
                        v['Disease'] = d_name
                        v['DiseaseCategory'] = d_c_name
                        res.append(v)

            else:
                disease_category_objs = DiseaseCategory.objects.all()
                res = []
                for d_c in disease_category_objs:
                    disease_objs = Disease.objects.filter(category=d_c)
                    d_c_name = d_c.name
                    for d in disease_objs:
                        d_name = d.name
                        objs = HospitalizedReport.objects.filter(disease=d)
                        for v in objs:
                            v = v.to_json()
                            v['Disease'] = d_name
                            v['DiseaseCategory'] = d_c_name
                            res.append(v)

        case _:

            pass

    return JsonResponse({"count": len(res), "docs": res})

