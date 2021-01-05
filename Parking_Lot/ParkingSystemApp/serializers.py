from rest_framework import serializers
from .models import *


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'Owner_name', 'full_parking_lots', 'property_list']


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'entry_time', 'vehicle_company', 'vehicle_model', 'colour', 'is_parked', 'checkout_time', 'time', 'paid',
                  'left',
                  'no_plate', 'park_id', 'slot_id', 'valet_assigned_id']


class ParkingLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingArea
        fields = ['id', 'unique_park_id', 'status', 'filled_parking_slots', 'property_Owner', 'slots']


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ['id', 'parked_car', 'slot_number', 'status']


class PoliceOrSecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceOrSecurity
        fields = ['id', 'officer_name', 'works_at', 'full_parking_lots']


class ValetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valet
        fields = ['id', 'valet_name', 'vehicle_assigned', 'is_Currently_Parking']


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'Driver_name', 'vehicle']
