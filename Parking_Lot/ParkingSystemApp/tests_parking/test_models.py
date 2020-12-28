from django.test import TestCase
from ..models import *


class OwnerAndPropertyTest(TestCase):
    def setUp(self):
        Owner.objects.create(Owner_name='cat')
        car_object = Car.objects.create(brand='Audi', vehicle_model='Q7', colour='black')
        slots = Slot.objects.create(row=1, column=5, parked_car=car_object)
        ParkingArea.objects.create(status="vacant", property_Owner="admin", slots=slots)

    def test_owner_creation(self):
        obj1 = Owner.objects.get(Owner_name='cat')
        self.assertEquals(obj1.Owner_name, 'cat')

    def test_parking_area(self):
        obj1 = ParkingArea.objects.get(property_Owner="admin")
        self.assertEquals(obj1.property_Owner, 'admin')

    def test_many_to_many_Owner_Property_relation(self):
        car_object = Car.objects.create(brand='Audi', vehicle_model='Q7', colour='black')
        slots = Slot.objects.create(row=1, column=5, parked_car=car_object)
        parking_lot1 = ParkingArea.objects.create(status="vacant", property_Owner="admin", slots=slots)
        parking_lot2 = ParkingArea.objects.create(status="vacant", property_Owner="admin", slots=slots)
        owner = Owner.objects.create(Owner_name="admin")
        owner.property_list.set([parking_lot1.pk, parking_lot2.pk])
        self.assertEqual(owner.property_list.count(), 2)


class CarTest(TestCase):
    def setUp(self):
        Car.objects.create(brand='Audi', vehicle_model='Q7', colour='black')

    def test_car_creation(self):
        obj1 = Car.objects.get(brand='Audi')
        self.assertEquals(obj1.vehicle_model, 'Q7')


class SlotTest(TestCase):
    def setUp(self):
        car_object = Car.objects.create(brand='Audi', vehicle_model='Q8', colour='aqua')
        Slot.objects.create(row=1, column=5, parked_car=car_object)

    def test_slot_creation(self):
        obj1 = Car.objects.get(colour='aqua')
        self.assertEquals(obj1.vehicle_model, 'Q8')


class Parking(TestCase):
    def test_parked_or_not(self):
        car_object = Car.objects.create(is_parked=True, brand='Bugatti', vehicle_model='chiron', colour='magenta')
        slots = Slot.objects.create(row=1, column=5, parked_car=car_object)
        ParkingArea.objects.create(property_Owner="admin", slots=slots)
        is_parked = Car.objects.get(id=car_object.id).is_parked
        self.assertEquals(True, is_parked)

    def test_unparked_or_not(self):
        car_object = Car.objects.create(is_parked=True, brand='Bugatti', vehicle_model='chiron', colour='magenta')
        slots = Slot.objects.create(row=1, column=5, parked_car=car_object)
        ParkingArea.objects.create(property_Owner="admin", slots=slots)
        car_object = Car.objects.get(is_parked=True, brand='Bugatti', vehicle_model='chiron', colour='magenta')
        car_object = Car.objects.get(id=car_object.id)
        car_object.is_parked = False
        car_object.save()
        slots = Slot.objects.get(row=1, column=5, parked_car=car_object)
        slots.parked_car = None
        slots.save()
        parking_lot_object = ParkingArea.objects.get(property_Owner="admin", slots=slots)
        parking_lot_object.slots = None
        parking_lot_object.save()
        is_parked = Car.objects.get(id=car_object.id).is_parked
        self.assertNotEqual(True, is_parked)
