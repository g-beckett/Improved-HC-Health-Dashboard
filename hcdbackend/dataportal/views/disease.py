from django.shortcuts import render
from django.http import Http404

from dataportal.models import Disease


def disease_all(request):

    context = {"diseases": Disease.objects.all()}

    return render(request, "dataportal/disease_all.html", context)


def disease_detail(request, pk):

    try:
        disease = Disease.objects.get(pk=pk)
    except Disease.DoesNotExist:
        raise Http404(f"Disease:{pk} does not exist")

    context = {"disease": disease}

    return render(request, "dataportal/disease_detail.html", context)
