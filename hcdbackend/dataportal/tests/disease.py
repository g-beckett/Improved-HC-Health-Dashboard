from django.test import TestCase
from dataportal.models import DiseaseCategory, Disease

"""
CRUD Unit Tests for Disease
"""


class DiseaseUnitTest(TestCase):

    def setUp(self):

        DiseaseCategory.objects.create(name="TestDC1", description="DC1Desc")
        dc = DiseaseCategory.objects.get(name="TestDC1")

        Disease.objects.create(name="TestDisease", description="DiseaseDesc", category=dc)
        Disease.objects.create(name="TestDisease2", description="DiseaseDesc2", category=dc)

    def test_read(self):

        all_objs = Disease.objects.all()

        # Check num of records equal to expected
        self.assertEqual(len(all_objs), 2)

        # Check what was created was what was expected
        found_names = []
        found_descriptions = []
        for v in all_objs:
            found_names.append(v.name)
            found_descriptions.append(v.description)

        self.assertEqual(found_names, ['TestDisease', 'TestDisease2'])
        self.assertEqual(found_descriptions, ['DiseaseDesc', 'DiseaseDesc2'])

    def test_update(self):

        dc1 = Disease.objects.get(name="TestDisease")
        dc1.name = "TestDiseaseUpdate"
        dc1.save()

        dc1 = Disease.objects.get(name="TestDiseaseUpdate")
        self.assertEqual(dc1.name, "TestDiseaseUpdate")

    def test_delete(self):

        dc2 = Disease.objects.get(name="TestDisease2")
        dc2.delete()

        all_objs = Disease.objects.all()

        # Check num of records equal to expected
        self.assertEqual(len(all_objs), 1)
