from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Car(models.Model):
    entry_time = models.DateTimeField(default=timezone.now)
    vehicle_company = models.CharField(default=None, max_length=100)
    vehicle_model = models.CharField(default=None, max_length=100)
    colour = models.CharField(default=None, max_length=100)
    checkout_time = models.DateTimeField(auto_now=True)
    is_parked = models.BooleanField(default=False)
    time = models.IntegerField(default=0)
    paid = models.BooleanField(default=False)
    left = models.BooleanField(default=False)
    no_plate = models.CharField(max_length=13, unique=True)
    park_id = models.IntegerField(validators=[MinValueValidator(1)], null=True, blank=True)
    slot_id = models.IntegerField(validators=[MinValueValidator(1)], null=True, blank=True)
    valet_assigned_id = models.IntegerField(validators=[MinValueValidator(1)], null=True, blank=True)

    def __str__(self):
        return f"{self.colour} - {self.vehicle_company} - {self.vehicle_model} - {self.no_plate} - is parked: {self.is_parked} - " \
               f"id: {self.id}"


class Slot(models.Model):
    STATUS_OPTIONS = (
        ('FULL', 'FULL'),
        ('VACANT', 'VACANT'),
    )
    row = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    column = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    parked_car = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True)
    slot_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    status = models.CharField(max_length=30, choices=STATUS_OPTIONS, null=True, blank=True)

    def __str__(self):
        return f"slot id: {self.id} number: [{self.slot_number} position [{self.row}{self.column}] - status: {self.status}]"


class ParkingArea(models.Model):
    STATUS_OPTIONS = (
        ('FULL', 'FULL'),
        ('VACANT', 'VACANT'),
    )
    unique_park_id = models.IntegerField(unique=True, validators=[MinValueValidator(1)])
    status = models.CharField(max_length=30, default="VACANT", choices=STATUS_OPTIONS, )
    filled_parking_slots = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=0,
                                               blank=True)
    property_Owner = models.CharField(max_length=30, default="admin")
    slots = models.ManyToManyField(Slot, blank=True, default="VACANT")

    def __str__(self):
        return f"id: {self.id} and unique id : {self.unique_park_id}"


class Owner(models.Model):
    Owner_name = models.CharField(max_length=30)
    property_list = models.ManyToManyField(ParkingArea, blank=True, default=None)
    full_parking_lots = models.ManyToManyField(ParkingArea, blank=True, related_name="fullPark", default=None)

    def __str__(self):
        return f"{self.Owner_name}"


class PoliceOrSecurity(models.Model):
    WORKS_AT_OPTIONS = (
        ('AIRPORT', 'AIRPORT'),
        ('POLICE', 'POLICE'),
    )
    officer_name = models.CharField(max_length=100)
    works_at = models.CharField(max_length=100, choices=WORKS_AT_OPTIONS)
    full_parking_lots = models.ManyToManyField(ParkingArea, blank=True, related_name="fullParkDetails", default=None)

    def __str__(self):
        return f"{self.officer_name} - {self.works_at}"


class Valet(models.Model):
    valet_name = models.CharField(max_length=100)
    vehicle_assigned = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True)
    is_Currently_Parking = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.valet_name} - status {self.is_Currently_Parking}  | id: {self.id}"


class Driver(models.Model):
    Driver_name = models.CharField(max_length=100)
    vehicle = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True)
    is_handicapped = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Driver_name} | -  vehicle: [ {self.vehicle} ] | handicapped?: {self.is_handicapped} | id: {self.id}"
