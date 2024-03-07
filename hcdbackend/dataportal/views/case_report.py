from django_tables2 import SingleTableView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from dataportal.models import CaseReport, CaseReportTable


class CaseReportListView(LoginRequiredMixin, SingleTableView):
    model = CaseReport
    table_class = CaseReportTable
    template_name = 'dataportal/generic_list.html'
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Case Reports'
        context['create_text'] = 'Submit New Case Report'
        context['create_link'] = 'dataportal:case-report-create'
        return context


class CaseReportDetailView(LoginRequiredMixin, DetailView):
    model = CaseReport
    template_name = 'dataportal/generic_detail.html'
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Case Report'
        context['update_text'] = 'Update'
        context['update_link'] = 'dataportal:case-report-update'
        context['delete_text'] = 'Delete'
        context['delete_link'] = 'dataportal:case-report-delete'
        return context


class CaseReportCreateView(LoginRequiredMixin, CreateView):
    model = CaseReport
    template_name = 'dataportal/generic_create.html'
    fields = ['disease',
              'case_count',
              'case_count_epi',
              'sex_female_count',
              'sex_male_count',
              'sex_unknown_count',
              'race_white_count',
              'race_black_count',
              'race_asian_count',
              'race_native_american_count',
              'race_other_count',
              'race_unknown_count',
              'ethnicity_hispanic_count',
              'ethnicity_non_hispanic_count',
              'ethnicity_unknown_count',
              'age_0_10_count',
              'age_11_20_count',
              'age_21_30_count',
              'age_31_40_count',
              'age_41_50_count',
              'age_51_60_count',
              'age_61_70_count',
              'age_71_80_count',
              'age_81_and_up_count',
              'age_unknown_count',
              'sex_present',
              'race_present',
              'ethnicity_present',
              'age_present',
              'report_start_date',
              'report_end_date',
              'report_submission_date']
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'New Case Report'
        return context

    def get_form(self, **kwargs):
        form = super(CaseReportCreateView, self).get_form()
        form.fields['report_start_date'].widget = forms.SelectDateWidget()
        form.fields['report_end_date'].widget = forms.SelectDateWidget()
        form.fields['report_submission_date'].widget = forms.SelectDateWidget()
        return form


class CaseReportUpdateView(LoginRequiredMixin, UpdateView):
    model = CaseReport
    template_name = 'dataportal/generic_update.html'
    fields = ['disease',
              'case_count',
              'case_count_epi',
              'sex_female_count',
              'sex_male_count',
              'sex_unknown_count',
              'race_white_count',
              'race_black_count',
              'race_asian_count',
              'race_native_american_count',
              'race_other_count',
              'race_unknown_count',
              'ethnicity_hispanic_count',
              'ethnicity_non_hispanic_count',
              'ethnicity_unknown_count',
              'age_0_10_count',
              'age_11_20_count',
              'age_21_30_count',
              'age_31_40_count',
              'age_41_50_count',
              'age_51_60_count',
              'age_61_70_count',
              'age_71_80_count',
              'age_81_and_up_count',
              'age_unknown_count',
              'sex_present',
              'race_present',
              'ethnicity_present',
              'age_present',
              'report_start_date',
              'report_end_date',
              'report_submission_date']
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Update Case Report'
        return context

    def get_form(self, **kwargs):
        form = super(CaseReportUpdateView, self).get_form()
        form.fields['report_start_date'].widget = forms.SelectDateWidget()
        form.fields['report_end_date'].widget = forms.SelectDateWidget()
        form.fields['report_submission_date'].widget = forms.SelectDateWidget()
        return form


class CaseReportDeleteView(LoginRequiredMixin, DeleteView):
    model = CaseReport
    template_name = 'dataportal/generic_delete.html'
    success_url = reverse_lazy('dataportal:case-report-list')
    login_url = '/accounts/login/'
    redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Delete Case Report'
        return context
