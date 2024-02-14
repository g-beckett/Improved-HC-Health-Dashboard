from django_tables2 import SingleTableView
from django.views.generic.detail import DetailView

from dataportal.models import DiseaseCategory, DiseaseCategoryTable


class DiseaseCategoryListView(SingleTableView):
    model = DiseaseCategory
    table_class = DiseaseCategoryTable
    template_name = 'dataportal/disease_category_list.html'


class DiseaseCategoryDetailView(DetailView):
    model = DiseaseCategory
    template_name = 'dataportal/disease_category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
