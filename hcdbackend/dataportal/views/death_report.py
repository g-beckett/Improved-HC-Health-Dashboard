from django_tables2 import SingleTableView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from dataportal.models import DeathReport, DeathReportTable


class DeathReportListView(LoginRequiredMixin, SingleTableView):
    model = DeathReport
    table_class = DeathReportTable
    template_name = 'dataportal/generic_list.html'
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Death Reports'
        context['create_text'] = 'Submit New Death Report'
        context['create_link'] = 'dataportal:death-report-create'
        return context


class DeathReportDetailView(LoginRequiredMixin, DetailView):
    model = DeathReport
    template_name = 'dataportal/generic_detail.html'
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Death Report'
        context['update_text'] = 'Update'
        context['update_link'] = 'dataportal:death-report-update'
        context['delete_text'] = 'Delete'
        context['delete_link'] = 'dataportal:death-report-delete'
        return context


class DeathReportCreateView(LoginRequiredMixin, CreateView):
    model = DeathReport
    template_name = 'dataportal/generic_create.html'
    fields = ['disease',
              'death_count',
              'report_start_date',
              'report_end_date',
              'report_submission_date']
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'New Death Report'
        return context

    def get_form(self, **kwargs):
        form = super(DeathReportCreateView, self).get_form()
        form.fields['report_start_date'].widget = forms.SelectDateWidget()
        form.fields['report_end_date'].widget = forms.SelectDateWidget()
        form.fields['report_submission_date'].widget = forms.SelectDateWidget()
        return form


class DeathReportUpdateView(LoginRequiredMixin, UpdateView):
    model = DeathReport
    template_name = 'dataportal/generic_update.html'
    fields = ['disease',
              'death_count',
              'report_start_date',
              'report_end_date',
              'report_submission_date']
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Update Death Report'
        return context

    def get_form(self, **kwargs):
        form = super(DeathReportUpdateView, self).get_form()
        form.fields['report_start_date'].widget = forms.SelectDateWidget()
        form.fields['report_end_date'].widget = forms.SelectDateWidget()
        form.fields['report_submission_date'].widget = forms.SelectDateWidget()
        return form


class DeathReportDeleteView(LoginRequiredMixin, DeleteView):
    model = DeathReport
    template_name = 'dataportal/generic_delete.html'
    success_url = reverse_lazy('dataportal:death-report-list')
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Delete Death Report'
        return context
