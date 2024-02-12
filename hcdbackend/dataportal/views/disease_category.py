from django.shortcuts import render

from dataportal.models import DiseaseCategory


def disease_category_all(request):
    context = {"disease_categories": DiseaseCategory.objects.all()}
    return render(request, "dataportal/disease_category_all.html", context)


def disease_category_detail(request, pk):
    context = {}
    return render(request, "dataportal/disease_category_detail.html", context)

