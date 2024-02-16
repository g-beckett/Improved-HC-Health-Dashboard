from django_tables2 import SingleTableView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from django.urls import reverse_lazy

from dataportal.models import ICUReport, ICUReportTable


class ICUReportListView(SingleTableView):
    model = ICUReport
    table_class = ICUReportTable
    template_name = 'dataportal/generic_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'ICU Reports'
        context['create_text'] = 'Submit New ICU Report'
        context['create_link'] = 'dataportal:icu-report-create'
        return context


class ICUReportDetailView(DetailView):
    model = ICUReport
    template_name = 'dataportal/generic_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'ICU Report'
        context['update_text'] = 'Update'
        context['update_link'] = 'dataportal:icu-report-update'
        context['delete_text'] = 'Delete'
        context['delete_link'] = 'dataportal:icu-report-delete'
        return context


class ICUReportCreateView(CreateView):
    model = ICUReport
    template_name = 'dataportal/generic_create.html'
    fields = ['disease',
              'icu_count',
              'report_start_date',
              'report_end_date',
              'report_submission_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'New ICU Report'
        return context

    def get_form(self, **kwargs):
        form = super(ICUReportCreateView, self).get_form()
        form.fields['report_start_date'].widget = forms.SelectDateWidget()
        form.fields['report_end_date'].widget = forms.SelectDateWidget()
        form.fields['report_submission_date'].widget = forms.SelectDateWidget()
        return form


class ICUReportUpdateView(UpdateView):
    model = ICUReport
    template_name = 'dataportal/generic_update.html'
    fields = ['disease',
              'icu_count',
              'report_start_date',
              'report_end_date',
              'report_submission_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Update ICU Report'
        return context

    def get_form(self, **kwargs):
        form = super(ICUReportUpdateView, self).get_form()
        form.fields['report_start_date'].widget = forms.SelectDateWidget()
        form.fields['report_end_date'].widget = forms.SelectDateWidget()
        form.fields['report_submission_date'].widget = forms.SelectDateWidget()
        return form


class ICUReportDeleteView(DeleteView):
    model = ICUReport
    template_name = 'dataportal/generic_delete.html'
    success_url = reverse_lazy('dataportal:icu-report-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = 'Delete ICU Report'
        return context