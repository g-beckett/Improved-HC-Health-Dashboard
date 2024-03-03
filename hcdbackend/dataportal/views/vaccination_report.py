from django_tables2 import SingleTableView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from dataportal.models import VaccinationReport, VaccinationReportTable


class VaccinationReportListView(LoginRequiredMixin, SingleTableView):
    model = VaccinationReport
    table_class = VaccinationReportTable
    template_name = 'dataportal/generic_list.html'
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Vaccination Reports'
        context['create_text'] = 'Submit New Vaccination Report'
        context['create_link'] = 'dataportal:vaccination-report-create'
        return context


class VaccinationReportDetailView(LoginRequiredMixin, DetailView):
    model = VaccinationReport
    template_name = 'dataportal/generic_detail.html'
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Vaccination Report'
        context['update_text'] = 'Update'
        context['update_link'] = 'dataportal:vaccination-report-update'
        context['delete_text'] = 'Delete'
        context['delete_link'] = 'dataportal:vaccination-report-delete'
        return context


class VaccinationReportCreateView(LoginRequiredMixin, CreateView):
    model = VaccinationReport
    template_name = 'dataportal/generic_create.html'
    fields = ['disease',
              'vaccination_count',
              'report_start_date',
              'report_end_date',
              'report_submission_date']
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'New Vaccination Report'
        return context

    def get_form(self, **kwargs):
        form = super(VaccinationReportCreateView, self).get_form()
        form.fields['report_start_date'].widget = forms.SelectDateWidget()
        form.fields['report_end_date'].widget = forms.SelectDateWidget()
        form.fields['report_submission_date'].widget = forms.SelectDateWidget()
        return form


class VaccinationReportUpdateView(LoginRequiredMixin, UpdateView):
    model = VaccinationReport
    template_name = 'dataportal/generic_update.html'
    fields = ['disease',
              'vaccination_count',
              'report_start_date',
              'report_end_date',
              'report_submission_date']
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Update Vaccination Report'
        return context

    def get_form(self, **kwargs):
        form = super(VaccinationReportUpdateView, self).get_form()
        form.fields['report_start_date'].widget = forms.SelectDateWidget()
        form.fields['report_end_date'].widget = forms.SelectDateWidget()
        form.fields['report_submission_date'].widget = forms.SelectDateWidget()
        return form


class VaccinationReportDeleteView(LoginRequiredMixin, DeleteView):
    model = VaccinationReport
    template_name = 'dataportal/generic_delete.html'
    success_url = reverse_lazy('dataportal:vaccination-report-list')
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Delete Vaccination Report'
        return context
