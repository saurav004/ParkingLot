from django.db import models
from django.utils import timezone


class Car(models.Model):
    entry_time = models.DateTimeField(default=timezone.now)
    brand = models.CharField(default=None, max_length=100)
    vehicle_model = models.CharField(default=None, max_length=100)
    colour = models.CharField(default=None, max_length=100)
    checkout_time = models.DateTimeField(auto_now=True)
    time = models.IntegerField(default=0)
    paid = models.BooleanField(default=False)
    left = models.BooleanField(default=False)
    no_plate = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.colour} - {self.brand} - {self.vehicle_model}"


class Slot(models.Model):
    parked_car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    row = models.IntegerField()
    column = models.IntegerField()

    def __str__(self):
        return f"{self.row} - {self.column}"


class ParkingArea(models.Model):
    status = models.CharField(max_length=30)
    property_Owner = models.CharField(max_length=30, default="admin")
    slots = models.ForeignKey(Slot, on_delete=models.DO_NOTHING, default=0)

    def __str__(self):
        return f"{self.status}"


class Owner(models.Model):
    Owner_name = models.CharField(max_length=30)
    property_list = models.ManyToManyField(ParkingArea)

    def __str__(self):
        return f"{self.Owner_name}"


class PoliceOrSecurity(models.Model):
    officer_name = models.CharField(max_length=100)
    works_at = models.CharField(max_length=100)
