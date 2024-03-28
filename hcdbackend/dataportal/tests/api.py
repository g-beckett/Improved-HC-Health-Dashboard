import json
from django.test import RequestFactory, TestCase

from dataportal.models import DiseaseCategory, Disease, CaseReport, DeathReport, HospitalizedReport
from dataportal.views import data_portal_api_2


"""
Unit Tests involved GET requests made to our API used by the dashboard. This tests URL param filtering.
"""


class APIUnitTest(TestCase):
    def setUp(self):
        DiseaseCategory.objects.create(name="TestDC1", description="DC1Desc")
        DiseaseCategory.objects.create(name="TestDC2", description="DC2Desc")

        dc = DiseaseCategory.objects.get(name="TestDC1")
        Disease.objects.create(name="TestDisease", description="DiseaseDesc", category=dc)
        Disease.objects.create(name="TestDisease2", description="DiseaseDesc", category=dc)

        d = Disease.objects.get(name="TestDisease")

        CaseReport.objects.create(disease=d, case_count=10, report_start_date='2020-07-01',
                                  report_end_date='2020-07-01', report_submission_date='2020-07-01')
        CaseReport.objects.create(disease=d, case_count=20, report_start_date='2020-08-01',
                                  report_end_date='2020-08-01', report_submission_date='2020-08-01')

        DeathReport.objects.create(disease=d, death_count=10, report_start_date='2020-07-01',
                                   report_end_date='2020-07-01', report_submission_date='2020-07-01')
        DeathReport.objects.create(disease=d, death_count=20, report_start_date='2020-08-01',
                                   report_end_date='2020-08-01', report_submission_date='2020-08-01')

        HospitalizedReport.objects.create(disease=d, icu_count=10, report_start_date='2020-07-01',
                                          report_end_date='2020-07-01', report_submission_date='2020-07-01')
        HospitalizedReport.objects.create(disease=d, icu_count=20, report_start_date='2020-08-01',
                                          report_end_date='2020-08-01', report_submission_date='2020-08-01')

        self.factory = RequestFactory()

    def test_get_disease_category(self):
        request = self.factory.get('/dataportal/_query2?type=disease_category')
        response = data_portal_api_2(request)
        self.assertEqual(response.status_code, 200)
        res = json.loads(response.content.decode())
        self.assertEqual(len(res['docs']), 2)

    def test_get_filter_disease(self):
        request = self.factory.get('/dataportal/_query2?type=disease&disease_category=TestDC1')
        response = data_portal_api_2(request)
        self.assertEqual(response.status_code, 200)
        res = json.loads(response.content.decode())
        self.assertEqual(len(res['docs']), 2)

    def test_get_filter_case_report_by_disease(self):
        request = self.factory.get('/dataportal/_query2?type=case_report&disease=TestDisease')
        response = data_portal_api_2(request)
        self.assertEqual(response.status_code, 200)
        res = json.loads(response.content.decode())
        self.assertEqual(len(res['docs']), 2)

    def test_get_filter_death_report_by_disease(self):
        request = self.factory.get('/dataportal/_query2?type=death_report&disease=TestDisease')
        response = data_portal_api_2(request)
        self.assertEqual(response.status_code, 200)
        res = json.loads(response.content.decode())
        self.assertEqual(len(res['docs']), 2)

    def test_get_filter_hospitalized_report_by_disease_category(self):
        request = self.factory.get('/dataportal/_query2?type=hospitalized_report&disease_category=TestDC1')
        response = data_portal_api_2(request)
        self.assertEqual(response.status_code, 200)
        res = json.loads(response.content.decode())
        self.assertEqual(len(res['docs']), 2)
