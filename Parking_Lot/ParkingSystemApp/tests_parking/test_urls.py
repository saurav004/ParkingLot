import unittest

from django.test import TestCase
from ..models import Owner, ParkingArea


class OwnerAndPropertyTest(TestCase):
    def setUp(self):
        Owner.objects.create(Owner_name='cat')

    def test_owner_creation(self):
        obj1 = Owner.objects.get(Owner_name="cat")
        self.assertEquals(obj1.Owner_name, 'cat')


if __name__ == '__main__':
    unittest.main()
