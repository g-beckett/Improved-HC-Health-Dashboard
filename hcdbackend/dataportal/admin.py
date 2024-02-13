from django.contrib import admin

from .models import Disease, DiseaseCategory, CaseReport

admin.site.register(Disease)
admin.site.register(DiseaseCategory)
admin.site.register(CaseReport)
