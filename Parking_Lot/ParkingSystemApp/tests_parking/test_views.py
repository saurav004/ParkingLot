from django.test import TestCase
from ..models import *
from ..views import *
import requests
import json


class TestOwnerApi(TestCase):
    URL = "http://127.0.0.1:8000/api/owner_api/"
    data = {}

    def test_owner_get_api(self):
        def get_owner_data(id=None):
            data = {'id': id}
            json_data = json.dumps(data)
            r = requests.get(url=self.URL, data=json_data)
            return r.json()

        data = get_owner_data(1)
        print(data)
        self.assertNotEqual(data, {})

