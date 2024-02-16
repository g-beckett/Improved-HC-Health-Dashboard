from django.urls import path

from . import views

app_name = 'dataportal'
urlpatterns = [
    path("", views.index, name="index"),

    path("_query", views.data_portal_api, name="dataportal-query"),

    path("disease_category", views.DiseaseCategoryListView.as_view(), name="disease-category-list"),
    path("disease_category/<int:pk>", views.DiseaseCategoryDetailView.as_view(), name="disease-category-detail"),
    path("disease_category/_create", views.DiseaseCategoryCreateView.as_view(), name="disease-category-create"),
    path("disease_category/<int:pk>/_update", views.DiseaseCategoryUpdateView.as_view(), name="disease-category-update"),
    path("disease_category/<int:pk>/_delete", views.DiseaseCategoryDeleteView.as_view(), name="disease-category-delete"),

    path("disease", views.DiseaseListView.as_view(), name="disease-list"),
    path("disease/<int:pk>", views.DiseaseDetailView.as_view(), name="disease-detail"),
    path("disease/_create", views.DiseaseCreateView.as_view(), name="disease-create"),
    path("disease/<int:pk>/_update", views.DiseaseUpdateView.as_view(), name="disease-update"),
    path("disease/<int:pk>/_delete", views.DiseaseDeleteView.as_view(), name="disease-delete"),

    path("case_report", views.CaseReportListView.as_view(), name="case-report-list"),
    path("case_report/<int:pk>", views.CaseReportDetailView.as_view(), name="case-report-detail"),
    path("case_report/_create", views.CaseReportCreateView.as_view(), name="case-report-create"),
    path("case_report/<int:pk>/_update", views.CaseReportUpdateView.as_view(), name="case-report-update"),
    path("case_report/<int:pk>/_delete", views.CaseReportDeleteView.as_view(), name="case-report-delete"),

    path("hospitalized_report", views.HospitalizedReportListView.as_view(), name="hospitalized-report-list"),
    path("hospitalized_report/<int:pk>", views.HospitalizedReportDetailView.as_view(), name="hospitalized-report-detail"),
    path("hospitalized_report/_create", views.HospitalizedReportCreateView.as_view(), name="hospitalized-report-create"),
    path("hospitalized_report/<int:pk>/_update", views.HospitalizedReportUpdateView.as_view(), name="hospitalized-report-update"),
    path("hospitalized_report/<int:pk>/_delete", views.HospitalizedReportDeleteView.as_view(), name="hospitalized-report-delete"),

    path("death_report", views.DeathReportListView.as_view(), name="death-report-list"),
    path("death_report/<int:pk>", views.DeathReportDetailView.as_view(), name="death-report-detail"),
    path("death_report/_create", views.DeathReportCreateView.as_view(), name="death-report-create"),
    path("death_report/<int:pk>/_update", views.DeathReportUpdateView.as_view(), name="death-report-update"),
    path("death_report/<int:pk>/_delete", views.DeathReportDeleteView.as_view(), name="death-report-delete"),

    path("icu_report", views.ICUReportListView.as_view(), name="icu-report-list"),
    path("icu_report/<int:pk>", views.ICUReportDetailView.as_view(), name="icu-report-detail"),
    path("icu_report/_create", views.ICUReportCreateView.as_view(), name="icu-report-create"),
    path("icu_report/<int:pk>/_update", views.ICUReportUpdateView.as_view(), name="icu-report-update"),
    path("icu_report/<int:pk>/_delete", views.ICUReportDeleteView.as_view(), name="icu-report-delete"),

    path("vaccination_report", views.VaccinationReportListView.as_view(), name="vaccination-report-list"),
    path("vaccination_report/<int:pk>", views.VaccinationReportDetailView.as_view(), name="vaccination-report-detail"),
    path("vaccination_report/_create", views.VaccinationReportCreateView.as_view(), name="vaccination-report-create"),
    path("vaccination_report/<int:pk>/_update", views.VaccinationReportUpdateView.as_view(), name="vaccination-report-update"),
    path("vaccination_report/<int:pk>/_delete", views.VaccinationReportDeleteView.as_view(), name="vaccination-report-delete")
]

