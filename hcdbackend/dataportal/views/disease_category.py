from django.shortcuts import render

from dataportal.models import DiseaseCategory


def disease_category_all(request):
    all_objects = DiseaseCategory.objects.all()
    context = {"disease_categories": all_objects}
    return render(request, "dataportal/disease_category_all.html", context)


def disease_category_detail(request):
    pass
