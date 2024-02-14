from django_tables2 import SingleTableView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from dataportal.models import Disease, DiseaseTable


class DiseaseListView(SingleTableView):
    model = Disease
    table_class = DiseaseTable
    template_name = 'dataportal/disease_list.html'


class DiseaseDetailView(DetailView):
    model = Disease
    template_name = 'dataportal/disease_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DiseaseCreateView(CreateView):
    model = Disease
    template_name = 'dataportal/disease_create.html'
    fields = ['name', 'description', 'category']
