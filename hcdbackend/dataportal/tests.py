from django.test import TestCase
from dataportal.models import DiseaseCategory, Disease

"""
To run,

python manage.py test
"""


class DiseaseCategoryTestCase(TestCase):

    def setUp(self):
        DiseaseCategory.objects.create(name="TestDC1", description="DC1Desc")
        DiseaseCategory.objects.create(name="TestDC2", description="DC2Desc")

    def test_read(self):
        all_objs = DiseaseCategory.objects.all()

        # Check num of records equal to expected
        self.assertEqual(len(all_objs), 2)

        # Check what was created was what was expected
        found_names = []
        found_descriptions = []
        for v in all_objs:
            found_names.append(v.name)
            found_descriptions.append(v.description)

        self.assertEqual(found_names, ['TestDC1', 'TestDC2'])
        self.assertEqual(found_descriptions, ['DC1Desc', 'DC2Desc'])

    def test_update(self):
        dc1 = DiseaseCategory.objects.get(name="TestDC1")
        dc1.name = "TestDC1_update"
        dc1.save()

        dc1 = DiseaseCategory.objects.get(name="TestDC1_update")
        self.assertEqual(dc1.name, "TestDC1_update")


