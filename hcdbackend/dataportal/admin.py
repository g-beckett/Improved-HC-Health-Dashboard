from django.contrib import admin

from .models import Disease, DiseaseCategory, CaseReport, HospitalizedReport, DeathReport, ICUReport, VaccinationReport

admin.site.register(Disease)
admin.site.register(DiseaseCategory)
admin.site.register(CaseReport)
admin.site.register(HospitalizedReport)
admin.site.register(DeathReport)
admin.site.register(ICUReport)
admin.site.register(VaccinationReport)
