from django_tables2 import SingleTableView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from dataportal.models import DiseaseCategory, DiseaseCategoryTable


class DiseaseCategoryListView(LoginRequiredMixin, SingleTableView):
    model = DiseaseCategory
    table_class = DiseaseCategoryTable
    template_name = 'dataportal/generic_list.html'
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Disease Categories'
        context['create_text'] = 'Add New Disease Category'
        context['create_link'] = 'dataportal:disease-category-create'
        return context


class DiseaseCategoryDetailView(LoginRequiredMixin, DetailView):
    model = DiseaseCategory
    template_name = 'dataportal/generic_detail.html'
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Disease Category'
        context['update_text'] = 'Update'
        context['update_link'] = 'dataportal:disease-category-update'
        context['delete_text'] = 'Delete'
        context['delete_link'] = 'dataportal:disease-category-delete'
        return context


class DiseaseCategoryCreateView(LoginRequiredMixin, CreateView):
    model = DiseaseCategory
    template_name = 'dataportal/generic_create.html'
    fields = ['name', 'description']
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'New Disease Category'
        return context


class DiseaseCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = DiseaseCategory
    template_name = 'dataportal/generic_update.html'
    fields = ['name', 'description']
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Update Disease Category'
        return context


class DiseaseCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = DiseaseCategory
    template_name = 'dataportal/generic_delete.html'
    success_url = reverse_lazy('dataportal:disease-category-list')
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Delete Disease Category'
        return context
