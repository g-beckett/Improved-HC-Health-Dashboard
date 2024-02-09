from django.urls import path

from . import views

app_name = 'dataportal'
urlpatterns = [
    path("", views.index, name="index"),
]

