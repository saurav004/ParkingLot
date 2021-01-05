from django.test import TestCase, Client
import json
from django.urls import reverse
from rest_framework import status

from ..models import Car

client = Client()


class Parking(TestCase):

    def setUp(self):
        self.car = Car.objects.create(brand='BMW', vehicle_model='Advanced', colour='black',
                                      park_id=25, slot_id=327)
        self.car.save()
        self.park_data = {
            "car_id": self.car.id,
            "slot_id": '327'
        }
        self.unpark_data = {
            "car_id": self.car.id,
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
