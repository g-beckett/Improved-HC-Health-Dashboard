from django_tables2 import SingleTableView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from dataportal.models import DiseaseCategory, DiseaseCategoryTable


class DiseaseCategoryListView(SingleTableView):
    model = DiseaseCategory
    table_class = DiseaseCategoryTable
    template_name = 'dataportal/generic_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Disease Categories'
        context['create_text'] = 'Add New Disease Category'
        context['create_link'] = 'dataportal:disease-category-create'
        return context


class DiseaseCategoryDetailView(DetailView):
    model = DiseaseCategory
    template_name = 'dataportal/generic_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Disease Category'
        context['update_text'] = 'Update'
        context['update_link'] = 'dataportal:disease-category-update'
        context['delete_text'] = 'Delete'
        context['delete_link'] = 'dataportal:disease-category-delete'
        return context


class DiseaseCategoryCreateView(CreateView):
    model = DiseaseCategory
    template_name = 'dataportal/generic_create.html'
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'New Disease Category'
        return context


class DiseaseCategoryUpdateView(UpdateView):
    model = DiseaseCategory
    template_name = 'dataportal/generic_update.html'
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Update Disease Category'
        return context


class DiseaseCategoryDeleteView(DeleteView):
    model = DiseaseCategory
    template_name = 'dataportal/generic_delete.html'
    success_url = reverse_lazy('dataportal:disease-category-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Delete Disease Category'
        return context
