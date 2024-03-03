from django_tables2 import SingleTableView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from dataportal.models import HospitalizedReport, HospitalizedReportTable


class HospitalizedReportListView(LoginRequiredMixin, SingleTableView):
    model = HospitalizedReport
    table_class = HospitalizedReportTable
    template_name = 'dataportal/generic_list.html'
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Hospitalized Reports'
        context['create_text'] = 'Submit New Hospitalization Report'
        context['create_link'] = 'dataportal:hospitalized-report-create'
        return context


class HospitalizedReportDetailView(LoginRequiredMixin, DetailView):
    model = HospitalizedReport
    template_name = 'dataportal/generic_detail.html'
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Hospitalized Report'
        context['update_text'] = 'Update'
        context['update_link'] = 'dataportal:hospitalized-report-update'
        context['delete_text'] = 'Delete'
        context['delete_link'] = 'dataportal:hospitalized-report-delete'
        return context


class HospitalizedReportCreateView(LoginRequiredMixin, CreateView):
    model = HospitalizedReport
    template_name = 'dataportal/generic_create.html'
    fields = ['disease',
              'inpatient_count',
              'under_investigation_count',
              'report_start_date',
              'report_end_date',
              'report_submission_date']
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'New Hospitalized Report'
        return context

    def get_form(self, **kwargs):
        form = super(HospitalizedReportCreateView, self).get_form()
        form.fields['report_start_date'].widget = forms.SelectDateWidget()
        form.fields['report_end_date'].widget = forms.SelectDateWidget()
        form.fields['report_submission_date'].widget = forms.SelectDateWidget()
        return form


class HospitalizedReportUpdateView(LoginRequiredMixin, UpdateView):
    model = HospitalizedReport
    template_name = 'dataportal/generic_update.html'
    fields = ['disease',
              'inpatient_count',
              'under_investigation_count',
              'report_start_date',
              'report_end_date',
              'report_submission_date']
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Update Hospitalized Report'
        return context

    def get_form(self, **kwargs):
        form = super(HospitalizedReportUpdateView, self).get_form()
        form.fields['report_start_date'].widget = forms.SelectDateWidget()
        form.fields['report_end_date'].widget = forms.SelectDateWidget()
        form.fields['report_submission_date'].widget = forms.SelectDateWidget()
        return form


class HospitalizedReportDeleteView(LoginRequiredMixin, DeleteView):
    model = HospitalizedReport
    template_name = 'dataportal/generic_delete.html'
    success_url = reverse_lazy('dataportal:hospitalized-report-list')
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Delete Hospitalized Report'
        return context
