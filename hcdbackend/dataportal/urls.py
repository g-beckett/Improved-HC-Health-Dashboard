from django.urls import path

from . import views

app_name = 'dataportal'
urlpatterns = [
    path("", views.index, name="index"),
    path("area", views.generic_all, name="area_all"),
    path("area/<int:pk>", views.generic_detail, name="area_detail"),
    path("animal", views.generic_all, name="animal_all"),
    path("animal/<int:pk>", views.generic_detail, name="animal_detail"),
    path("species", views.generic_all, name="species_all"),
    path("species/<int:pk>", views.generic_detail, name="species_detail"),
    path("animal_report", views.animal_report_all, name="animal_report_all"),
]

