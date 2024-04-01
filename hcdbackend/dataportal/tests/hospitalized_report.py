from django.test import TestCase
from dataportal.models import DiseaseCategory, Disease, HospitalizedReport

"""
CRUD Unit Tests for HospitalizedReport
"""


class HospitalizedReportUnitTest(TestCase):

    def setUp(self):

        DiseaseCategory.objects.create(name="TestDC1", description="DC1Desc")
        dc = DiseaseCategory.objects.get(name="TestDC1")

        Disease.objects.create(name="TestDisease", description="DiseaseDesc", category=dc)
        d = Disease.objects.get(name="TestDisease")

        HospitalizedReport.objects.create(disease=d, icu_count=10, report_start_date='2020-07-01',
                                          report_end_date='2020-07-01', report_submission_date='2020-07-01')
        HospitalizedReport.objects.create(disease=d, icu_count=20, report_start_date='2020-08-01',
                                          report_end_date='2020-08-01', report_submission_date='2020-08-01')

    def test_read(self):

        all_objs = HospitalizedReport.objects.all()

        # Check num of records equal to expected
        self.assertEqual(len(all_objs), 2)

        # Check what was created was what was expected
        total_icu = 0
        for v in all_objs:
            total_icu += v.icu_count

        self.assertEqual(total_icu, 30)

    def test_update(self):

        report = HospitalizedReport.objects.all()[0]

        report.icu_count = report.icu_count + 10
        report.save()

        all_objs = HospitalizedReport.objects.all()

        # Check num of records equal to expected
        self.assertEqual(len(all_objs), 2)

        # Check what was created was what was expected
        total_icu = 0
        for v in all_objs:
            total_icu += v.icu_count

        self.assertEqual(total_icu, 40)

    def test_delete(self):

        report = HospitalizedReport.objects.all()[0]
        report.delete()

        all_objs = HospitalizedReport.objects.all()

        # Check num of records equal to expected
        self.assertEqual(len(all_objs), 1)
