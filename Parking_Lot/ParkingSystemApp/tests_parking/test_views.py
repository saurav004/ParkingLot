from django.test import TestCase
from ..models import *
import requests
import json


class Parking(TestCase):

    def test_parked_or_not(self):
        url = "http://127.0.0.1:8000/api/park_api/"

        def park_car():
            data = {
                "car_id": 39,
                "park_id": 25,
                "slot_id": 426
            }
            json_data = json.dumps(data)
            r = requests.post(url=url, data=json_data,)
            return r.json()

        data = park_car()
        car_id = 39
        car_object = Car.objects.get(id=car_id)
        self.assertEquals(True, car_object.is_parked)

    def test_unparked_or_not(self):
        car_id = 40
        car_object = Car.objects.get(id=car_id)
        self.assertEquals(False, car_object.is_parked)


