from django.db import models

from .disease import Disease
from .disease_category import DiseaseCategory


class CaseReport(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    disease_category = models.ForeignKey(DiseaseCategory, on_delete=models.CASCADE)

    case_count = models.IntegerField(default=0)
    case_count_epi = models.IntegerField(default=0)

    sex_female_count = models.IntegerField(default=0)
    sex_male_count = models.IntegerField(default=0)
    sex_unknwon_count = models.IntegerField(default=0)

    race_white_count = models.IntegerField(default=0)
    race_black_count = models.IntegerField(default=0)
    race_asian_count = models.IntegerField(default=0)
    race_native_american_count = models.IntegerField(default=0)
    race_other_count = models.IntegerField(default=0)
    race_unknown_count = models.IntegerField(default=0)
    

    ethnicity_hispanic_count = models.IntegerField(default=0)
    ethnicity_non_hispanic_count = models.IntegerField(default=0)
    ethnicity_unknown_count = models.IntegerField(default=0)


    age_0_10_count = models.IntegerField(default=0)
    age_11_20_count = models.IntegerField(default=0)
    age_21_30_count = models.IntegerField(default=0)
    age_31_40_count = models.IntegerField(default=0)
    age_41_50_count = models.IntegerField(default=0)
    age_51_60_count = models.IntegerField(default=0)
    age_61_70_count = models.IntegerField(default=0)
    age_71_80_count = models.IntegerField(default=0)
    age_81_and_up_count = models.IntegerField(default=0)
    age_unknown_count = models.IntegerField(default=0)
    
    start_date = models.DateField()
    end_date = models.DateField()

