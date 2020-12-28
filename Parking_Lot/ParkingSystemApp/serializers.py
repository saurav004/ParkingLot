from rest_framework import serializers
from .models import *


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'Owner_name', 'property_list']


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'entry_time', 'brand', 'vehicle_model', 'colour', 'checkout_time', 'time', 'paid', 'left', 'no_plate']


class ParkingLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingArea
        fields = ['id', 'status', 'property_Owner', 'slots']


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ['id', 'parked_car', 'row', 'column']
