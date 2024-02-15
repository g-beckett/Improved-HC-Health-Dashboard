from django_tables2 import SingleTableView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from dataportal.models import Disease, DiseaseTable


class DiseaseListView(SingleTableView):
    model = Disease
    table_class = DiseaseTable
    template_name = 'dataportal/generic_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Diseases'
        context['create_text'] = 'Add New Disease'
        context['create_link'] = 'dataportal:disease-create'
        return context


class DiseaseDetailView(DetailView):
    model = Disease
    template_name = 'dataportal/generic_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Disease'
        context['update_text'] = 'Update'
        context['update_link'] = 'dataportal:disease-update'
        context['delete_text'] = 'Delete'
        context['delete_link'] = 'dataportal:disease-delete'
        return context


class DiseaseCreateView(CreateView):
    model = Disease
    template_name = 'dataportal/generic_create.html'
    fields = ['name', 'description', 'category']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'New Disease'
        return context


class DiseaseUpdateView(UpdateView):
    model = Disease
    template_name = 'dataportal/generic_update.html'
    fields = ['name', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Update Disease'
        return context


class DiseaseDeleteView(DeleteView):
    model = Disease
    template_name = 'dataportal/generic_delete.html'
    success_url = reverse_lazy('dataportal:disease-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Delete Disease'
        return context
