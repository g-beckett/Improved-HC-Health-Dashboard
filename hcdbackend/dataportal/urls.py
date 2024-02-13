from django.urls import path

from . import views

app_name = 'dataportal'
urlpatterns = [
    path("", views.index, name="index"),
    path("disease_category", views.disease_category_all, name="disease_category_all"),
    path("disease_category/<int:pk>", views.disease_category_detail, name="disease_category_detail"),
    path("disease", views.disease_all, name="disease_all"),
    path("disease/<int:pk>", views.disease_detail, name="disease_detail"),
    path("case_report", views.case_report_all, name="case_report_all"),
    path("case_report/<int:pk>", views.case_report_detail, name="case_report_detail")
]

