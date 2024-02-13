from django.shortcuts import render
from django.http import Http404

from dataportal.models import DiseaseCategory


def disease_category_all(request):

    context = {"disease_categories": DiseaseCategory.objects.all()}

    return render(request, "dataportal/disease_category_all.html", context)


def disease_category_detail(request, pk):

    try:
        disease_category = DiseaseCategory.objects.get(pk=pk)
    except DiseaseCategory.DoesNotExist:
        raise Http404(f"DiseaseCategory:{pk} does not exist")

    context = {"disease_category": disease_category}

    return render(request, "dataportal/disease_category_detail.html", context)

