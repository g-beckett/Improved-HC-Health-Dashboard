from django.contrib import admin

from .models import Species, Animal, Area, AnimalReport
from .models import Disease, DiseaseCategory

admin.site.register(Species)
admin.site.register(Animal)
admin.site.register(Area)
admin.site.register(AnimalReport)

admin.site.register(Disease)
admin.site.register(DiseaseCategory)

