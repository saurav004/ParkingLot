from django.test import TestCase
from ..models import *


class OwnerAndPropertyTest(TestCase):
    def setUp(self):
        Owner.objects.create(Owner_name='cat')
        car_object = Car.objects.create(vehicle_company='Audi', vehicle_model='Q7', colour='black',
                                        no_plate='AB 12 CD 1234')
        slots = Slot.objects.create(slot_number=0, parked_car=car_object)
        ParkingArea.objects.create(unique_park_id=9, status="VACANT", property_Owner="Kumar Saurav")

    def test_OwnerModel_WhenOwnerCreated_NameShouldBeEqualToGivenName(self):
        obj1 = Owner.objects.get(Owner_name='cat')
        self.assertEquals(obj1.Owner_name, 'cat')

    def test_OwnerModel_WhenSearchedForDataNotCreated_ShouldRaiseException(self):
        with self.assertRaises(Owner.DoesNotExist):
            Owner.objects.get(Owner_name='dog')

    def test_ParkingModel_WhenObjectCreated_DataShouldBeSameAsGiven(self):
        obj1 = ParkingArea.objects.get(property_Owner="Kumar Saurav")
        self.assertEquals(obj1.property_Owner, 'Kumar Saurav')

    def test_ParkingModel_WhenSearchedForDataNotCreated_ShouldRaiseException(self):
        with self.assertRaises(ParkingArea.DoesNotExist):
            ParkingArea.objects.get(property_Owner="admin")

    def test_many_to_many_Owner_Property_relation(self):
        parking_lot1 = ParkingArea.objects.create(unique_park_id=5, status="VACANT", property_Owner="Kumar Saurav",
                                                  )
        parking_lot2 = ParkingArea.objects.create(unique_park_id=6, status="VACANT", property_Owner="KUMAR SAURAV",
                                                  )
        owner_obj = Owner.objects.create(Owner_name="Kumar Saurav")
        owner_obj.property_list.set([parking_lot1.pk, parking_lot2.pk])
        self.assertEqual(owner_obj.property_list.count(), 2)

    def test_ManyToManyRelation_WhenNotAdded_ShouldBeEmpty(self):
        owner_obj = Owner.objects.create(Owner_name="Kumar Saurav")
        owner_obj.save()
        self.assertEqual(owner_obj.property_list.count(), 0)


class CarTest(TestCase):
    def setUp(self):
        Car.objects.create(vehicle_company='Audi', vehicle_model='Q7', colour='black', no_plate='GH 12 CD 1234')

    def test_car_creation(self):
        obj1 = Car.objects.get(vehicle_company='Audi')
        self.assertEquals(obj1.vehicle_model, 'Q7')


class SlotTest(TestCase):
    def setUp(self):
        car_object = Car.objects.create(vehicle_company='Audi', vehicle_model='Q8', colour='aqua')
        Slot.objects.create(slot_number=0, parked_car=car_object)

    def test_slot_creation(self):
        obj1 = Slot.objects.get(slot_number=0)
        self.assertEquals(obj1.parked_car.vehicle_model, 'Q8')
