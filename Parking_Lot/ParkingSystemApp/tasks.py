from __future__ import absolute_import, unicode_literals
from celery import shared_task
from time import sleep

from .models import *


@shared_task
def add(x, y):
    return x + y


@shared_task
def notify_owner_car_is_parked(park_object_id):
    park_object = ParkingArea.objects.get(id=park_object_id)
    owner_object = Owner.objects.get(Owner_name=park_object.property_Owner)
    owner_object.full_parking_lots.add(park_object)


@shared_task
def notify_airport_security_car_is_parked(park_object_id):
    park_object = ParkingArea.objects.get(id=park_object_id)
    for obj in PoliceOrSecurity.objects.all():
        if obj.works_at == "AIRPORT":
            obj.full_parking_lots.add(park_object)

@shared_task
def notify_owner_car_is_unparked(park_object_id):
    park_object = ParkingArea.objects.get(id=park_object_id)
    owner_object = Owner.objects.get(Owner_name=park_object.property_Owner)
    owner_object.full_parking_lots.remove(park_object)


@shared_task
def notify_airport_security_car_is_unparked(park_object_id):
    park_object = ParkingArea.objects.get(id=park_object_id)
    for obj in PoliceOrSecurity.objects.all():
        if obj.works_at == "AIRPORT":
            obj.full_parking_lots.remove(park_object)
