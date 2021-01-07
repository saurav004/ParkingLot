from django.test import TestCase, Client
import json
from django.urls import reverse
from rest_framework import status
from ..models import Car, ParkingArea, Slot, Driver, Valet, Owner, PoliceOrSecurity
from ..serializers import VehicleSerializer

client = Client()


class Parking(TestCase):

    def setUp(self):
        self.car = Car.objects.create(vehicle_company='BMW', vehicle_model='Advanced', colour='black',
                                      no_plate="AB 12 CD 1234")
        self.park = ParkingArea.objects.create(unique_park_id=10, status="VACANT", property_Owner="Kumar Saurav")
        for i in range(1, 101):
            slot = Slot.objects.create(slot_number=i)
            self.park.status = "VACANT"
            self.park.slots.add(slot)
        self.driver = Driver.objects.create(Driver_name="something", vehicle=self.car)
        self.valet = Valet.objects.create(valet_name="koi bhi")
        self.car2 = Car.objects.create(vehicle_company='BMW', vehicle_model='Advanced', colour='black',
                                       park_id=self.park.id, slot_id=self.park.slots.all()[0].id,
                                       no_plate="AB 12 CD 1237", valet_assigned_id=self.valet.id)
        self.park_data = {
            "car_id": self.car.id,
            "driver_id": self.driver.id
        }
        self.unpark_data = {
            "car_id": self.car2.id,
        }

    def test_park(self):
        response = client.post(
            reverse('park'),
            data=json.dumps(self.park_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unpark(self):
        response = client.post(
            reverse('unpark'),
            data=json.dumps(self.unpark_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class OwnerTest(TestCase):
    def setUp(self):
        self.Owner1 = Owner.objects.create(Owner_name="something")
        self.Owner2 = Owner.objects.create(Owner_name="SomethingElse")

        self.single_owner_data = {
            "id": self.Owner1.id,
        }
        self.owner_post_data = {
            "Owner_name": "Kumar Saurav",
            "property_list": [],
        }
        self.owner_put_data = {
            "id": self.Owner1.id,
            "Owner_name": "Lorem Ipsum",
            "full_parking_lots": []
        }
        self.owner_patch_data = {
            "id": self.Owner1.id,
            "Owner_name": "ftbt ubyft",
        }
        self.owner_delete_data = {
            "id": self.Owner1.id,
        }

    def test_Owner_get_Api(self):
        response = client.get(
            reverse('owner_list'),
            data=self.single_owner_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Owner_post_Api(self):
        response = client.post(
            reverse('owner_list'),
            data=json.dumps(self.owner_post_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Owner_put_Api(self):
        response = client.put(
            reverse('owner_list'),
            data=json.dumps(self.owner_put_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Owner_patch_Api(self):
        response = client.patch(
            reverse('owner_list'),
            data=json.dumps(self.owner_patch_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Owner_delete_Api(self):
        response = client.delete(
            reverse('owner_list'),
            data=json.dumps(self.owner_delete_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ParkingAreaTest(TestCase):
    def setUp(self):
        self.park = ParkingArea.objects.create(unique_park_id=11, status="VACANT", property_Owner="Kumar Saurav")
        self.get_data = {
            "id": self.park.id
        }
        self.post_data = {
            "unique_park_id": 12
        }
        self.put_data = {
            "id": self.park.id,
            "unique_park_id": 11,
            "status": "VACANT",
            "property_Owner": "Kumar Saurav"
        }
        self.patch_data = {
            "id": self.park.id,
            "unique_park_id": 11,
            "status": "VACANT",
        }
        self.delete_data = {
            "id": self.park.id,
        }

    def test_ParkingLot_get_Api(self):
        response = client.get(
            reverse('parking_list'),
            data=self.get_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ParkingLot_post_Api(self):
        response = client.post(
            reverse('parking_list'),
            data=json.dumps(self.post_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ParkingLot_put_Api(self):
        response = client.put(
            reverse('parking_list'),
            data=json.dumps(self.put_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ParkingLot_patch_Api(self):
        response = client.patch(
            reverse('parking_list'),
            data=json.dumps(self.patch_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ParkingLot_delete_Api(self):
        response = client.delete(
            reverse('parking_list'),
            data=json.dumps(self.delete_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class VehicleTest(TestCase):
    def setUp(self):
        self.vehicle = Car.objects.create(vehicle_company='Audi', vehicle_model='Q7', colour='black',
                                          no_plate='AB 12 CD 1434')
        self.get_data = {
            "id": 1
        }
        self.post_data = {
            'vehicle_company': 'Audi',
            "vehicle_model": 'Q8',
            'colour': 'silver'
        }
        self.put_data = {
            "id": self.vehicle.id,
            'vehicle_company': 'Tesla',
            "vehicle_model": 'Electric',
            'colour': 'black'
        }
        self.patch_data = {
            "id": self.vehicle.id,
            'vehicle_company': 'Tesla',
            "vehicle_model": 'Electric'
        }
        self.delete_data = {
            "id": self.vehicle.id,
        }

    def test_Vehicle_get_Api(self):
        response = client.get(
            reverse('vehicle_list'),
            data=self.get_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vehicle_post_Api(self):
        response = client.post(
            reverse('vehicle_list'),
            data=json.dumps(self.post_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vehicle_put_Api(self):
        response = client.put(
            reverse('vehicle_list'),
            data=json.dumps(self.put_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vehicle_patch_Api(self):
        response = client.patch(
            reverse('vehicle_list'),
            data=json.dumps(self.patch_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vehicle_delete_Api(self):
        response = client.delete(
            reverse('vehicle_list'),
            data=json.dumps(self.delete_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SlotTest(TestCase):
    def setUp(self):
        self.car = Car.objects.create(vehicle_company='BMW', vehicle_model='Advanced', colour='black',
                                      no_plate="ZX 67 CD 1234")
        self.slots = Slot.objects.create(slot_number=0, parked_car=self.car)
        self.get_data = {
            "id": 1
        }
        serializer = VehicleSerializer(self.car)
        self.post_data = {
            "parked_car": serializer.data,
            "slot_number": 1,
            "status": "VACANT"
        }
        self.put_data = {
            "id": self.slots.id,
            "slot_number": 1,
            "status": "FULL"
        }
        self.patch_data = {
            "id": self.slots.id,
            "status": "VACANT",
        }
        self.delete_data = {
            "id": self.slots.id,
        }

    def test_Slot_get_Api(self):
        response = client.get(
            reverse('slot_list'),
            data=self.get_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Slot_post_Api(self):
        response = client.post(
            reverse('slot_list'),
            data=json.dumps(self.post_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vehicle_put_Api(self):
        response = client.put(
            reverse('slot_list'),
            data=json.dumps(self.put_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vehicle_patch_Api(self):
        response = client.patch(
            reverse('slot_list'),
            data=json.dumps(self.patch_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vehicle_delete_Api(self):
        response = client.delete(
            reverse('slot_list'),
            data=json.dumps(self.delete_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PoliceApiTest(TestCase):
    def setUp(self):
        self.police_or_security = PoliceOrSecurity.objects.create(officer_name="Shaktiman", works_at="AIRPORT")
        self.get_data = {
            "id": 1
        }
        self.post_data = {
            "officer_name": "JAMES BOND",
            "works_at": "AIRPORT",
        }
        self.put_data = {
            "id": self.police_or_security.id,
            "officer_name": "someName",
            "works_at": "AIRPORT",
        }
        self.patch_data = {
            "id": self.police_or_security.id,
            "works_at": "POLICE",
        }
        self.delete_data = {
            "id": self.police_or_security.id,
        }

    def test_Police_get_Api(self):
        response = client.get(
            reverse('police_or_security_list'),
            data=self.get_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Police_post_Api(self):
        response = client.post(
            reverse('police_or_security_list'),
            data=json.dumps(self.post_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Police_put_Api(self):
        response = client.put(
            reverse('police_or_security_list'),
            data=json.dumps(self.put_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Police_patch_Api(self):
        response = client.patch(
            reverse('police_or_security_list'),
            data=json.dumps(self.patch_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Police_delete_Api(self):
        response = client.delete(
            reverse('police_or_security_list'),
            data=json.dumps(self.delete_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ValetTest(TestCase):
    def setUp(self):
        self.car = Car.objects.create(vehicle_company='BMW', vehicle_model='Advanced', colour='black',
                                      no_plate="ZX 67 CD 9911")
        serializer = VehicleSerializer(self.car)
        self.valet = Valet.objects.create(valet_name="Shaktiman", vehicle_assigned=self.car)
        self.get_data = {
            "id": 1
        }
        self.post_data = {
            "valet_name": "AB",
            "vehicle_assigned": serializer.data,
        }
        self.put_data = {
            "id": self.valet.id,
            "valet_name": "CD",
            "vehicle_assigned": serializer.data,
        }
        self.patch_data = {
            "id": self.valet.id,
            "Owner_name": "ftbt ubyft",
        }
        self.delete_data = {
            "id": self.valet.id,
        }

    def test_valet_get_Api(self):
        response = client.get(
            reverse('valet_list'),
            data=self.get_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valet_post_Api(self):
        response = client.post(
            reverse('valet_list'),
            data=json.dumps(self.post_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valet_put_Api(self):
        response = client.put(
            reverse('valet_list'),
            data=json.dumps(self.put_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valet_patch_Api(self):
        response = client.patch(
            reverse('valet_list'),
            data=json.dumps(self.patch_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valet_delete_Api(self):
        response = client.delete(
            reverse('valet_list'),
            data=json.dumps(self.delete_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DriverTest(TestCase):
    def setUp(self):
        self.car = Car.objects.create(vehicle_company='BMW', vehicle_model='Advanced', colour='black',
                                      no_plate="LL 67 CD 9911")
        serializer = VehicleSerializer(self.car)
        self.driver = Driver.objects.create(Driver_name="Shaktiman", vehicle=self.car)
        self.get_data = {
            "id": 1
        }
        self.post_data = {
            "Driver_name": "AB",
            "vehicle_assigned": serializer.data,
        }
        self.put_data = {
            "id": self.driver.id,
            "Driver_name": "CD",
            "vehicle": serializer.data,
            "is_handicapped": True
        }
        self.patch_data = {
            "id": self.driver.id,
            "is_handicapped": False
        }
        self.delete_data = {
            "id": self.driver.id,
        }

    def test_driver_get_Api(self):
        response = client.get(
            reverse('driver_list'),
            data=self.get_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_driver_post_Api(self):
        response = client.post(
            reverse('driver_list'),
            data=json.dumps(self.post_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_driver_put_Api(self):
        response = client.put(
            reverse('driver_list'),
            data=json.dumps(self.put_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_driver_patch_Api(self):
        response = client.patch(
            reverse('driver_list'),
            data=json.dumps(self.patch_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_driver_delete_Api(self):
        response = client.delete(
            reverse('driver_list'),
            data=json.dumps(self.delete_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DetailQueryAPIs(TestCase):

    def setUp(self):
        self.park = ParkingArea.objects.create(unique_park_id=12, status="VACANT", property_Owner="Kumar Saurav")
        self.vehicle = Car.objects.create(id=20, vehicle_company='Maruti', vehicle_model='800', colour='blue',
                                          no_plate="VK 34 CD 6413")
        self.car_data = {
            "car_id": self.vehicle.id
        }
        self.park_data = {
            "park_id": self.park.id
        }
        self.minutes_back_in_time = {
            "time_ago": "30"
        }
        self.vehicle_company = {
            "vehicle_company": "Maruti"
        }
        self.vehicle_company_and_colour = {
            "vehicle_company": "Maruti",
            "colour": "blue"
        }
        self.colour_of_vehicle = {
            "colour": "blue"
        }

    def test_find_my_car_api(self):
        response = client.get(
            reverse('find_car'),
            data=self.car_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_car_entry_time_api(self):
        response = client.get(
            reverse('entry_time'),
            data=self.car_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_all_vehicle_info_in_the_lot(self):
        response = client.get(
            reverse('all_vehicle_info_in_the_lot'),
            data=self.park_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vehicle_info_back_in_time(self):
        response = client.get(
            reverse('vehicle_info_back_in_time'),
            data=self.minutes_back_in_time
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vehicle_details(self):
        response = client.get(
            reverse('vehicle_info'),
            data=self.vehicle_company
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_location_number_parking_attendant_info_Api(self):
        response = client.get(
            reverse('vehicle_investigation'),
            data=self.vehicle_company
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_location_info(self):
        response = client.get(
            reverse('location_info'),
            data=self.colour_of_vehicle
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)