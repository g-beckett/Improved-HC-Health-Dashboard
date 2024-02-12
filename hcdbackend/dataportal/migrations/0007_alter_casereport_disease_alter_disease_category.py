# Generated by Django 5.0.1 on 2024-02-12 21:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataportal', '0006_alter_casereport_disease_alter_disease_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casereport',
            name='disease',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataportal.disease'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataportal.diseasecategory'),
        ),
    ]
