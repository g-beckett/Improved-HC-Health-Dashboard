from django.test import TestCase
from dataportal.models import DiseaseCategory, Disease, DeathReport

"""
CRUD Unit Tests for DeathReport
"""


class DeathReportUnitTest(TestCase):

    def setUp(self):

        DiseaseCategory.objects.create(name="TestDC1", description="DC1Desc")
        dc = DiseaseCategory.objects.get(name="TestDC1")

        Disease.objects.create(name="TestDisease", description="DiseaseDesc", category=dc)
        d = Disease.objects.get(name="TestDisease")

        DeathReport.objects.create(disease=d, death_count=10, report_start_date='2020-07-01',
                                   report_end_date='2020-07-01', report_submission_date='2020-07-01')
        DeathReport.objects.create(disease=d, death_count=20, report_start_date='2020-08-01',
                                   report_end_date='2020-08-01', report_submission_date='2020-08-01')

    def test_read(self):

        all_objs = DeathReport.objects.all()

        # Check num of records equal to expected
        self.assertEqual(len(all_objs), 2)

        # Check what was created was what was expected
        total_deaths = 0
        for v in all_objs:
            total_deaths += v.death_count

        self.assertEqual(total_deaths, 30)

    def test_update(self):

        report = DeathReport.objects.all()[0]

        report.death_count = report.death_count + 10
        report.save()

        all_objs = DeathReport.objects.all()

        # Check num of records equal to expected
        self.assertEqual(len(all_objs), 2)

        # Check what was created was what was expected
        total_deaths = 0
        for v in all_objs:
            total_deaths += v.death_count

        self.assertEqual(total_deaths, 40)

    def test_delete(self):

        report = DeathReport.objects.all()[0]
        report.delete()

        all_objs = DeathReport.objects.all()

        # Check num of records equal to expected
        self.assertEqual(len(all_objs), 1)
