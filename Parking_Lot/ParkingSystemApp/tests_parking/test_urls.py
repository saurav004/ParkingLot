
from django.test import TestCase
from ..models import *


class OwnerAndPropertyTest(TestCase):
    def setUp(self):
        Owner.objects.create(Owner_name='cat')
        slots = Slot.objects.create(row=1, column=5)
        ParkingArea.objects.create(status="vacant", property_Owner="admin", slots=slots)

    def test_owner_creation(self):
        obj1 = Owner.objects.get(Owner_name="cat")
        self.assertEquals(obj1.Owner_name, 'cat')

    def test_parking_area(self):
        obj1 = ParkingArea.objects.get(property_Owner="admin")
        self.assertEquals(obj1.property_Owner, 'admin')

    def test_many_to_many_Owner_Property_relation(self):
        parking_lot1 = ParkingArea.objects.create(status="vacant", property_Owner="admin")
        parking_lot2 = ParkingArea.objects.create(status="vacant", property_Owner="admin")
        owner = Owner.objects.create(Owner_name="admin")
        owner.property_list.set([parking_lot1.pk, parking_lot2.pk])
        self.assertEqual(owner.property_list.count(), 2)
