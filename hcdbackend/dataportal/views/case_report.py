from django_tables2 import SingleTableView
from django.views.generic.detail import DetailView

from dataportal.models import CaseReport, CaseReportTable


class CaseReportListView(SingleTableView):
    model = CaseReport
    table = CaseReportTable
    template_name = 'dataportal/case_report_list.html'


class CaseReportDetailView(DetailView):
    model = CaseReport
    template_name = 'dataportal/case_report_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
