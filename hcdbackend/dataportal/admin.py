from django.contrib import admin

from .models import Disease, DiseaseCategory, CaseReport, HospitalizedReport

admin.site.register(Disease)
admin.site.register(DiseaseCategory)
admin.site.register(CaseReport)
admin.site.register(HospitalizedReport)
