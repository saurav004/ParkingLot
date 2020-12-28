from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import OwnerSerializer, ParkingLotSerializer, SlotSerializer, VehicleSerializer


# Create your views here.

def home(request):
    return HttpResponse('<div class="container"><h1>Home</h1></div>')


class OwnerApi(APIView):
    def get(self, request, pk=None):
        id = pk
        if id is not None:
            owner_object = Owner.objects.get(id=id)
            serializer = OwnerSerializer(owner_object)
            return Response(serializer.data)
        owner_object = Owner.objects.all()
        serializer = OwnerSerializer(owner_object, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'})
        return Response({'msg': serializer.errors})

    def put(self, request, pk=None):
        owner_object = Owner.objects.get(pk=pk)
        serializer = OwnerSerializer(owner_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Uploaded'})
        return Response(serializer.errors)

    def patch(self, request, pk=None):
        owner_object = Owner.objects.get(pk=pk)
        serializer = OwnerSerializer(owner_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Uploaded'})
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        owner_object = Owner.objects.get(pk=pk)
        owner_object.delete()
        return Response({'msg': 'Data Deleted'})


class ParkingApi(APIView):
    def get(self, request, pk=None):
        id = pk
        if id is not None:
            object1 = ParkingArea.objects.get(id=id)
            serializer = ParkingLotSerializer(object1)
            return Response(serializer.data)
        object1 = ParkingArea.objects.all()
        serializer = ParkingLotSerializer(object1, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = ParkingLotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'})
        return Response({'msg': serializer.errors})

    def put(self, request, pk=None):
        object1 = ParkingArea.objects.get(pk=pk)
        serializer = ParkingLotSerializer(object1, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Uploaded'})
        return Response(serializer.errors)

    def patch(self, request, pk=None):
        object1 = ParkingArea.objects.get(pk=pk)
        serializer = ParkingLotSerializer(object1, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Uploaded'})
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        object1 = ParkingArea.objects.get(pk=pk)
        object1.delete()
        return Response({'msg': 'Data Deleted'})


class VehicleApi(APIView):
    def get(self, request, pk=None):
        id = pk
        if id is not None:
            object1 = Car.objects.get(id=id)
            serializer = VehicleSerializer(object1)
            return Response(serializer.data)
        object1 = Car.objects.all()
        serializer = VehicleSerializer(object1, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'})
        return Response({'msg': serializer.errors})

    def put(self, request, pk=None):
        object1 = Car.objects.get(pk=pk)
        serializer = VehicleSerializer(object1, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Uploaded'})
        return Response(serializer.errors)

    def patch(self, request, pk=None):
        object1 = Car.objects.get(pk=pk)
        serializer = VehicleSerializer(object1, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Uploaded'})
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        object1 = Car.objects.get(pk=pk)
        object1.delete()
        return Response({'msg': 'Data Deleted'})


class SlotApi(APIView):
    def get(self, request, pk=None):
        id = pk
        if id is not None:
            object1 = Slot.objects.get(id=id)
            serializer = SlotSerializer(object1)
            return Response(serializer.data)
        object1 = Slot.objects.all()
        serializer = SlotSerializer(object1, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = SlotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'})
        return Response({'msg': serializer.errors})

    def put(self, request, pk=None):
        object1 = Slot.objects.get(pk=pk)
        serializer = SlotSerializer(object1, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Uploaded'})
        return Response(serializer.errors)

    def patch(self, request, pk=None):
        object1 = Slot.objects.get(pk=pk)
        serializer = SlotSerializer(object1, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Uploaded'})
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        object1 = Slot.objects.get(pk=pk)
        object1.delete()
        return Response({'msg': 'Data Deleted'})


