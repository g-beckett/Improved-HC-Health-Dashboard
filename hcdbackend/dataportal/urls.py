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
    path("case_report/<int:pk>/_delete", views.CaseReportDeleteView.as_view(), name="case-report-delete")
]

