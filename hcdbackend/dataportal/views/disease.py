from django_tables2 import SingleTableView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from dataportal.models import Disease, DiseaseTable

"""
CRUD Views for Disease
"""


class DiseaseListView(LoginRequiredMixin, SingleTableView):
    model = Disease
    table_class = DiseaseTable
    template_name = 'dataportal/generic_list.html'
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Diseases'
        context['create_text'] = 'Add New Disease'
        context['create_link'] = 'dataportal:disease-create'
        return context


class DiseaseDetailView(LoginRequiredMixin, DetailView):
    model = Disease
    template_name = 'dataportal/generic_detail.html'
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Disease'
        context['update_text'] = 'Update'
        context['update_link'] = 'dataportal:disease-update'
        context['delete_text'] = 'Delete'
        context['delete_link'] = 'dataportal:disease-delete'
        return context


class DiseaseCreateView(LoginRequiredMixin, CreateView):
    model = Disease
    template_name = 'dataportal/generic_create.html'
    fields = ['name', 'description', 'category', 'cdc_link', 'wiki_link', 'mayo_link']
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'New Disease'
        return context


class DiseaseUpdateView(LoginRequiredMixin, UpdateView):
    model = Disease
    template_name = 'dataportal/generic_update.html'
    fields = ['name', 'description', 'cdc_link', 'wiki_link', 'mayo_link']
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Update Disease'
        return context


class DiseaseDeleteView(LoginRequiredMixin, DeleteView):
    model = Disease
    template_name = 'dataportal/generic_delete.html'
    success_url = reverse_lazy('dataportal:disease-list')
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Delete Disease'
        return context
