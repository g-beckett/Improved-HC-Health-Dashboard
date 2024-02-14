from django.urls import path

from . import views

app_name = 'dataportal'
urlpatterns = [
    path("", views.index, name="index"),
    path("disease_category", views.DiseaseCategoryListView.as_view(), name="disease-category-list"),
    path("disease_category/<int:pk>", views.DiseaseCategoryDetailView.as_view(), name="disease-category-detail"),
    path("disease_category/_create", views.DiseaseCategoryCreateView.as_view(), name="disease-category-create"),
    path("disease", views.DiseaseListView.as_view(), name="disease-list"),
    path("disease/<int:pk>", views.DiseaseDetailView.as_view(), name="disease-detail"),
    path("disease/_create", views.DiseaseCreateView.as_view(), name="disease-create"),
    path("case_report", views.CaseReportListView.as_view(), name="case-report-list"),
    path("case_report/<int:pk>", views.CaseReportDetailView.as_view(), name="case-report-detail"),
    path("case_report/_create", views.CaseReportCreateView.as_view(), name="case-report-create")
]

