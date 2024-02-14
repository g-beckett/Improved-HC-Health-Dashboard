from django_tables2 import SingleTableView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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


class DiseaseCategoryCreateView(CreateView):
    model = DiseaseCategory
    template_name = 'dataportal/disease_category_create.html'
    fields = ['name', 'description']


class DiseaseCategoryUpdateView(UpdateView):
    model = DiseaseCategory
    template_name = 'dataportal/disease_category_update.html'
    fields = ['name', 'description']


class DiseaseCategoryDeleteView(DeleteView):
    model = DiseaseCategory
    template_name = 'dataportal/disease_category_delete.html'
    success_url = reverse_lazy('dataportal:disease-category-list')
