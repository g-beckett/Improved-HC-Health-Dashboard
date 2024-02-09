from django.shortcuts import render

from dataportal.models import AnimalReport


def animal_report_all(request):
    reports = AnimalReport.objects.all()
    context = {"reports": reports}
    return render(request, "dataportal/animal_report_all.html", context)
