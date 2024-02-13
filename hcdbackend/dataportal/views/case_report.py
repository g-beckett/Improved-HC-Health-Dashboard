from django.shortcuts import render
from django.http import Http404

from dataportal.models import CaseReport


def case_report_all(request):

    context = {"case_reports": CaseReport.objects.all()}

    return render(request, "dataportal/case_report_all.html", context)


def case_report_detail(request, pk):

    try:
        case_report = CaseReport.objects.get(pk=pk)
    except CaseReport.DoesNotExist:
        raise Http404(f"Case Report:{pk} does not exist")

    context = {"case_report": case_report}

    return render(request, "dataportal/case_report_detail.html", context)
