from django.shortcuts import render
from django.http import JsonResponse
# from django.core import serializers

from dataportal.models import AnimalReport


def animal_report_all(request):
    reports = AnimalReport.objects.all()
    context = {"reports": reports}
    return render(request, "dataportal/animal_report_all.html", context)


def animal_report_api(request):
    reports = AnimalReport.objects.all()
    data = [v.to_json() for v in reports]  # Note try serializers again maybe?
    return JsonResponse({"docs": data, "docs_count": len(data)})
