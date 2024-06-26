# Generated by Django 5.0.1 on 2024-03-07 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataportal', '0004_disease_cdc_link_disease_mayo_link_disease_wiki_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='casereport',
            name='age_present',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='casereport',
            name='ethnicity_present',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='casereport',
            name='race_present',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='casereport',
            name='sex_present',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='age_0_10_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='age_11_20_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='age_21_30_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='age_31_40_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='age_41_50_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='age_51_60_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='age_61_70_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='age_71_80_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='age_81_and_up_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='age_present',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='age_unknown_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='ethnicity_hispanic_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='ethnicity_non_hispanic_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='ethnicity_present',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='ethnicity_unknown_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='race_asian_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='race_black_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='race_native_american_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='race_other_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='race_present',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='race_unknown_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='race_white_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='sex_female_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='sex_male_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='sex_present',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='deathreport',
            name='sex_unknown_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hospitalizedreport',
            name='icu_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='deathreport',
            name='death_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hospitalizedreport',
            name='inpatient_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hospitalizedreport',
            name='under_investigation_count',
            field=models.IntegerField(default=0),
        ),
    ]
