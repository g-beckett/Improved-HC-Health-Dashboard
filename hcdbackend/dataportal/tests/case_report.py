from django.test import TestCase
from dataportal.models import DiseaseCategory, Disease, CaseReport

"""
CRUD Unit Tests for CaseReport
"""


class CaseReportUnitTest(TestCase):

    def setUp(self):

        DiseaseCategory.objects.create(name="TestDC1", description="DC1Desc")
        dc = DiseaseCategory.objects.get(name="TestDC1")

        Disease.objects.create(name="TestDisease", description="DiseaseDesc", category=dc)
        d = Disease.objects.get(name="TestDisease")

        CaseReport.objects.create(disease=d, case_count=10, report_start_date='2020-07-01',
                                  report_end_date='2020-07-01', report_submission_date='2020-07-01')
        CaseReport.objects.create(disease=d, case_count=20, report_start_date='2020-08-01',
                                  report_end_date='2020-08-01', report_submission_date='2020-08-01')

    def test_read(self):

        all_objs = CaseReport.objects.all()

        # Check num of records equal to expected
        self.assertEqual(len(all_objs), 2)

        # Check what was created was what was expected
        total_cases = 0
        for v in all_objs:
            total_cases += v.case_count

        self.assertEqual(total_cases, 30)

    def test_update(self):

        report = CaseReport.objects.all()[0]

        report.case_count = report.case_count + 10
        report.save()

        all_objs = CaseReport.objects.all()

        # Check num of records equal to expected
        self.assertEqual(len(all_objs), 2)

        # Check what was created was what was expected
        total_cases = 0
        for v in all_objs:
            total_cases += v.case_count

        self.assertEqual(total_cases, 40)

    def test_delete(self):

        report = CaseReport.objects.all()[0]
        report.delete()

        all_objs = CaseReport.objects.all()

        # Check num of records equal to expected
        self.assertEqual(len(all_objs), 1)
