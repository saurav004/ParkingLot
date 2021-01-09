# Logger imports
import logging

from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import APIView

from .serializers import *
from .tasks import *

logger = logging.getLogger('django')


def home(request):
    return HttpResponse('<div class="container"><h1>Home</h1></div>')


class OwnerApi(APIView):
    def get(self, request):
        id = request.data.get('id')
        if id is not None:
            owner_object = Owner.objects.get(id=id)
            serializer = OwnerSerializer(owner_object)
            logger.debug('owner objects found and returned')
            return Response(status=HTTP_200_OK, data=serializer.data)
        owner_object = Owner.objects.all()
        serializer = OwnerSerializer(owner_object, many=True)
        logger.debug('list of owner object found and returned')
        return Response(status=HTTP_200_OK, data=serializer.data)

    def post(self, request):
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug('owner object created with the data provided')
            return Response({'msg': 'Data created'})
        logger.debug(serializer.errors)
        return Response(status=HTTP_200_OK, data=serializer.errors)

    def put(self, request):
        id = request.data.get('id')
        owner_object = Owner.objects.get(id=id)
        serializer = OwnerSerializer(owner_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.debug('Owner object updated')
            return Response(status=HTTP_200_OK, data={'msg': 'Complete Data Uploaded'})
        logger.debug(serializer.errors)
        return Response(serializer.errors)

    def patch(self, request):
        id = request.data.get('id')
        owner_object = Owner.objects.get(id=id)
        serializer = OwnerSerializer(owner_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.debug('Owner object updated')
            return Response({'msg': 'Partial Data Uploaded'})
        logger.debug(serializer.errors)
        return Response(serializer.errors)

    def delete(self, request):
        id = request.data.get('id')
        owner_object = Owner.objects.get(id=id)
        owner_object.delete()
        logger.debug('Owner object deleted')
        return Response({'msg': 'Data Deleted'})


class ParkingApi(APIView):
    def get(self, request):
        id = request.data.get('id')
        if id is not None:
            object1 = ParkingArea.objects.get(id=id)
            serializer = ParkingLotSerializer(object1)
            logger.debug('owner objects found and returned')
            return Response(serializer.data)
        object1 = ParkingArea.objects.all()
        serializer = ParkingLotSerializer(object1, many=True)
        logger.debug('list of owner objects found and returned')
        return Response(serializer.data)

    def post(self, request):
        serializer = ParkingLotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            park_id = request.data.get('unique_park_id')
            parking_object = ParkingArea.objects.get(unique_park_id=park_id)
            count = 0
            for i in range(1, 11):
                for j in range(1, 11):
                    count = count + 1
                    slot = Slot.objects.create(slot_number=count, row=i, column=j)
                    slot.save()
            parking_object.status = "VACANT"
            parking_object.slots.add(slot)
            parking_object.save()
            logger.debug('Park object created with data given')
            return Response({'msg': 'Data created'})
        logger.debug(serializer.errors)
        return Response({'msg': serializer.errors})

    def put(self, request):
        id = request.data.get('id')
        object1 = ParkingArea.objects.get(id=id)
        serializer = ParkingLotSerializer(object1, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.debug('Park object updated with data given')
            return Response({'msg': 'Complete Data Uploaded'})
        logger.debug(serializer.errors)
        return Response(serializer.errors)

    def patch(self, request):
        id = request.data.get('id')
        object1 = ParkingArea.objects.get(id=id)
        serializer = ParkingLotSerializer(object1, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.debug('Park object updated with data given')
            return Response({'msg': 'Partial Data Uploaded'})
        logger.debug(serializer.errors)
        return Response(serializer.errors)

    def delete(self, request):
        id = request.data.get('id')
        object1 = ParkingArea.objects.get(id=id)
        object1.delete()
        logger.debug(f'Park object of id : {id} deleted')
        return Response({'msg': 'Data Deleted'})


class VehicleApi(APIView):
    def get(self, request):
        id = request.data.get('id')
        if id is not None:
            object1 = Car.objects.get(id=id)
            serializer = VehicleSerializer(object1)
            logger.debug('Vehicle object found and returned')
            return Response(serializer.data)
        object1 = Car.objects.all()
        serializer = VehicleSerializer(object1, many=True)
        logger.debug(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug('Vehicle object created with data provided')
            return Response({'msg': 'Data created'})
        logger.debug(serializer.errors)
        return Response({'msg': serializer.errors})

    def put(self, request):
        id = request.data.get('id')
        object1 = Car.objects.get(id=id)
        serializer = VehicleSerializer(object1, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.debug('Vehicle object updated with data provided')
            return Response({'msg': 'Complete Data Uploaded'})
        logger.debug(serializer.errors)
        return Response(serializer.errors)

    def patch(self, request):
        id = request.data.get('id')
        object1 = Car.objects.get(id=id)
        serializer = VehicleSerializer(object1, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.debug('Vehicle object updated with data provided')
            return Response({'msg': 'Partial Data Uploaded'})
        logger.debug(serializer.errors)
        return Response(serializer.errors)

    def delete(self, request):
        id = request.data.get('id')
        object1 = Car.objects.get(id=id)
        object1.delete()
        logger.debug(f'object with id: {id} deleted')
        return Response({'msg': 'Data Deleted'})


class SlotApi(APIView):
    def get(self, request):
        id = request.data.get('id')
        if id is not None:
            object1 = Slot.objects.get(id=id)
            serializer = SlotSerializer(object1)
            logger.debug('Slot Object found and returned')
            return Response(serializer.data)
        object1 = Slot.objects.all()
        serializer = SlotSerializer(object1, many=True)
        logger.debug('list of owner objects found and returned')
        return Response(serializer.data)

    def post(self, request):
        serializer = SlotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug('Slot object created with data provided')
            return Response({'msg': 'Data created'})
        logger.debug(serializer.errors)
        return Response({'msg': serializer.errors})

    def put(self, request):
        id = request.data.get('id')
        object1 = Slot.objects.get(id=id)
        serializer = SlotSerializer(object1, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.debug('Slot object updated with data provided')
            return Response({'msg': 'Complete Data Uploaded'})
        logger.debug(serializer.errors)
        return Response(serializer.errors)

    def patch(self, request):
        id = request.data.get('id')
        object1 = Slot.objects.get(id=id)
        serializer = SlotSerializer(object1, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.debug('Slot object updated with data provided')
            return Response({'msg': 'Partial Data Uploaded'})
        logger.debug(serializer.errors)
        return Response(serializer.errors)

    def delete(self, request):
        id = request.data.get('id')
        object1 = Slot.objects.get(id=id)
        object1.delete()
        logger.debug(f'Slot object with id: {id} deleted')
        return Response({'msg': 'Data Deleted'})


class PoliceOrSecurityApi(APIView):
    def get(self, request):
        id = request.data.get('id')
        if id is not None:
            object1 = PoliceOrSecurity.objects.get(id=id)
            serializer = PoliceOrSecuritySerializer(object1)
            logger.debug('PoliceOrSecurity Object found and returned')
            return Response(serializer.data)
        object1 = PoliceOrSecurity.objects.all()
        serializer = PoliceOrSecuritySerializer(object1, many=True)
        logger.debug('list of PoliceOrSecurity Object found and returned')
        return Response(serializer.data)

    def post(self, request):
        serializer = PoliceOrSecuritySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug('PoliceOrSecurity object created with data provided')
            return Response({'msg': 'Data created'})
        logger.debug(serializer.errors)
        return Response({'msg': serializer.errors})

    def put(self, request):
        id = request.data.get('id')
        object1 = PoliceOrSecurity.objects.get(id=id)
        serializer = PoliceOrSecuritySerializer(object1, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.debug('PoliceOrSecurity object updated with data provided')
            return Response({'msg': 'Complete Data Uploaded'})
        logger.debug(serializer.errors)
        return Response(serializer.errors)

    def patch(self, request):
        id = request.data.get('id')
        object1 = PoliceOrSecurity.objects.get(id=id)
        serializer = PoliceOrSecuritySerializer(object1, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.debug('PoliceOrSecurity object updated with data provided')
            return Response({'msg': 'Partial Data Uploaded'})
        logger.debug(serializer.errors)
        return Response(serializer.errors)

    def delete(self, request):
        id = request.data.get('id')
        object1 = PoliceOrSecurity.objects.get(id=id)
        object1.delete()
        logger.debug(f'PoliceOrSecurity object with id : {id} deleted')
        return Response(status=HTTP_200_OK, data={'msg': 'Data Deleted'})


class ValetApi(APIView):
    def get(self, request):
        id = request.data.get('id')
        if id is not None:
            object1 = Valet.objects.get(id=id)
            serializer = ValetSerializer(object1)
            logger.debug('Valet/parking Attendant Object found and returned')
            return Response(status=HTTP_200_OK, data=serializer.data)
        object1 = Valet.objects.all()
        serializer = ValetSerializer(object1, many=True)
        logger.debug('list of Valet Object found and returned')
        return Response(status=HTTP_200_OK, data=serializer.data)

    def post(self, request):
        serializer = ValetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug('Valet Object created with data provided')
            return Response(status=HTTP_200_OK, data={'msg': 'Data created'})
        logger.debug(serializer.errors)
        return Response({'msg': serializer.errors})

    def put(self, request):
        id = request.data.get('id')
        object1 = Valet.objects.get(id=id)
        serializer = ValetSerializer(object1, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.debug('Valet Object updated with data provided')
            return Response({'msg': 'Complete Data Uploaded'})
        logger.debug(serializer.errors)
        return Response(serializer.errors)

    def patch(self, request):
        id = request.data.get('id')
        object1 = Valet.objects.get(id=id)
        serializer = ValetSerializer(object1, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.debug('Valet Object updated with data provided')
            return Response({'msg': 'Partial Data Uploaded'})
        logger.debug(serializer.errors)
        return Response(serializer.errors)

    def delete(self, request):
        id = request.data.get('id')
        object1 = Valet.objects.get(id=id)
        object1.delete()
        logger.debug(f'Valet object with id : {id} deleted')
        return Response({'msg': 'Data Deleted'})


class DriverApi(APIView):
    def get(self, request):
        id = request.data.get('id')
        if id is not None:
            object1 = Driver.objects.get(id=id)
            serializer = DriverSerializer(object1)
            logger.debug('Driver Object found and returned')
            return Response(serializer.data)
        object1 = Driver.objects.all()
        serializer = DriverSerializer(object1, many=True)
        logger.debug('list of Driver Object found and returned')
        return Response(serializer.data)

    def post(self, request):
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug('Driver Object created with data provided')
            return Response({'msg': 'Data created'})
        logger.debug(serializer.errors)
        return Response({'msg': serializer.errors})

    def put(self, request):
        id = request.data.get('id')
        object1 = Driver.objects.get(id=id)
        serializer = DriverSerializer(object1, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.debug('Driver Object updated with data provided')
            return Response({'msg': 'Complete Data Uploaded'})
        logger.debug(serializer.errors)
        return Response(serializer.errors)

    def patch(self, request):
        id = request.data.get('id')
        object1 = Driver.objects.get(id=id)
        serializer = DriverSerializer(object1, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.debug('Driver Object updated with data provided')
            return Response({'msg': 'Partial Data Uploaded'})
        logger.debug(serializer.errors)
        return Response(serializer.errors)

    def delete(self, request):
        id = request.data.get('id')
        object1 = Driver.objects.get(id=id)
        object1.delete()
        logger.debug(f'Driver object with id : {id} deleted')
        return Response({'msg': 'Data Deleted'})


@api_view(['GET'])
@csrf_exempt
def find_my_car_api(request):
    car_id = request.data.get('car_id')
    car_object = Car.objects.get(id=car_id)
    return Response(status=HTTP_200_OK, data={'park': car_object.park_id, 'slot': car_object.slot_id})


@api_view(['GET'])
@csrf_exempt
def car_entry_time(request):
    car_id = request.data.get('car_id')
    car_object = Car.objects.get(id=car_id)
    return Response(status=HTTP_200_OK, data={'car_entry_time': car_object.entry_time})


@csrf_exempt
@api_view(['POST'])
def park_my_car(request):
    driver_object = Driver.objects.get(id=request.data.get('driver_id'))
    parking_lot_object = ParkingArea.objects.first()
    if driver_object.is_handicapped:
        parking_objects_list = ParkingArea.objects.all().order_by('id')
    else:
        parking_objects_list = ParkingArea.objects.all()
    for park in parking_objects_list:
        if parking_lot_object.filled_parking_slots > park.filled_parking_slots:
            parking_lot_object = park
    parking_lot_id = parking_lot_object.id
    parking_lot_object = ParkingArea.objects.get(id=parking_lot_id)
    if parking_lot_object.filled_parking_slots < 100:
        parking_lot_object.filled_parking_slots = parking_lot_object.filled_parking_slots + 1
        if parking_lot_object.filled_parking_slots == 100:
            parking_lot_object.status = "FULL"
            notify_owner_car_is_parked.delay(parking_lot_object.id)
            notify_airport_security_car_is_parked.delay(parking_lot_object.id)
        parking_lot_object.save()
        slots = None
        if driver_object.is_handicapped:
            slot_obj_list = parking_lot_object.slots.all().order_by('-id')
            should_break = False
            for i in range(1, 11):
                for j in range(1, 11):
                    for slot_obj in slot_obj_list:
                        if slot_obj.row == i and slot_obj.column == j:
                            if slot_obj.status == "VACANT" or slot_obj.status is None:
                                slots = slot_obj
                                should_break = True
                    if should_break:
                        break
                if should_break:
                    break
        else:
            slot_obj_list = parking_lot_object.slots.all()
            for slot_obj in slot_obj_list:
                if slot_obj.status == "VACANT" or slot_obj.status is None:
                    slots = slot_obj
        if slots is None:
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR, data={'msg': 'no slot is VACANT'})
        else:
            slot_id = slots.id
        parking_attendant = None
        for obj in Valet.objects.all():
            if not obj.is_Currently_Parking:
                parking_attendant = obj
                break
        if parking_attendant is None:
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR, data={'msg': 'no valet is free now'})
        car_id = request.data.get('car_id')
        car_object = Car.objects.get(id=car_id)
        car_object.is_parked = True
        car_object.valet_assigned_id = parking_attendant.id
        parking_attendant.vehicle_assigned = car_object
        parking_attendant.is_Currently_Parking = True
        parking_attendant.save()
        slots.parked_car = car_object
        slots.status = "FULL"
        slots.save()
        car_object.slot_id = slot_id
        car_object.park_id = parking_lot_id
        car_object.save()
        serializer = VehicleSerializer(car_object)
        return Response(status=HTTP_201_CREATED, data=serializer.data)
    else:
        return Response(status=HTTP_400_BAD_REQUEST, data={'msg': 'park full'})


@api_view(['POST'])
@csrf_exempt
def unpark_my_car(request):
    car_id = request.data['car_id']
    if car_id is not None:
        car_object = Car.objects.get(id=car_id)
        if car_object:
            slot_id = car_object.slot_id
            slot_object = Slot.objects.get(id=slot_id)
            slot_object.parked_car = None
            slot_object.status = "VACANT"
            slot_object.save()
            park_id = car_object.park_id
            park_object = ParkingArea.objects.get(id=park_id)
            valet_id = car_object.valet_assigned_id
            valet_object = Valet.objects.get(id=valet_id)
            valet_object.is_Currently_Parking = False
            valet_object.vehicle_assigned = None
            valet_object.save()
            park_object.filled_parking_slots = park_object.filled_parking_slots - 1
            if park_object.status == "FULL":
                park_object.status = "VACANT"
                notify_owner_car_is_unparked.delay(park_object.id)
                notify_airport_security_car_is_unparked.delay(park_object.id)
            park_object.save()
            car_object.is_parked = False
            car_object.slot_id = None
            car_object.park_id = None
            car_object.valet_assigned_id = None
            car_object.save()
            serializer = VehicleSerializer(car_object)
            return Response(status=HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=HTTP_400_BAD_REQUEST, data={"msg": 'Car not Found'})
    else:
        return Response(status=HTTP_400_BAD_REQUEST, data={"msg": "car id provided is null"})


@api_view(['GET'])
@csrf_exempt
def get_vehicle_location_info(request):
    colour = request.data.get('colour_of_car')
    data = {}
    for vehicle in Car.objects.filter(colour=colour):
        data[vehicle.id] = {"colour": vehicle.colour, "park_id": vehicle.park_id, "slot_id": vehicle.slot_id}
    return Response(status=HTTP_200_OK, data=data)


@api_view(['GET'])
@csrf_exempt
def get_location_number_parking_attendant_info(request):
    vehicle_company = request.data.get('vehicle_company')
    colour = request.data.get('colour')
    data = {}
    for vehicle in Car.objects.filter(vehicle_company=vehicle_company, colour=colour, ):
        valet_obj = Valet.objects.get(id=vehicle.valet_assigned_id)
        parking_attendant_name = valet_obj.valet_name
        data[vehicle.id] = {"no_plate": vehicle.no_plate, "parking_attendant": parking_attendant_name,
                            "colour": vehicle.colour, "park_id": vehicle.park_id,
                            "slot_id": vehicle.slot_id}
    return Response(status=HTTP_200_OK, data=data)


@api_view(['GET'])
@csrf_exempt
def get_vehicle_details(request):
    vehicle_company = request.data.get('vehicle_company')
    data = {}
    count = 0
    for vehicle in Car.objects.filter(vehicle_company=vehicle_company):
        serializer = VehicleSerializer(vehicle)
        count = count + 1
        data[count] = serializer.data
    return Response(status=HTTP_200_OK, data=data)


@api_view(['GET'])
@csrf_exempt
def get_vehicle_info_parked_before_time_given(request):
    time_ago = request.data.get('time_ago')
    time_ago = timezone.now() - timezone.timedelta(minutes=time_ago)
    data = Car.objects.filter(entry_time__gt=time_ago)
    serializer = VehicleSerializer(data, many=True)
    return Response(status=HTTP_200_OK, data=serializer.data)


@api_view(['GET'])
@csrf_exempt
def get_info_of_all_vehicles_parked_in_the_lot(request):
    park_id = request.data.get('park_id')
    data = Car.objects.filter(park_id=park_id)
    serializer = VehicleSerializer(data, many=True)
    return Response(status=HTTP_200_OK, data=serializer.data)


@api_view(['GET'])
@csrf_exempt
def get_location_and_info_of_vehicles_in_row(request):
    row_and_column_mapping_with_letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
                                           'J': 10}
    row = request.data.get('row')
    park_id = request.data.get('park_id')
    row = row_and_column_mapping_with_letters.get(row)
    park = ParkingArea.objects.get(id=park_id)
    slot_list = park.slots.all()
    data = {}
    count = 0
    for slot_obj in slot_list:
        if slot_obj.row == row:
            if slot_obj.parked_car is not None:
                count = count + 1
                serializer = VehicleSerializer(slot_obj.parked_car)
                data[count] = serializer.data
    return Response(status=HTTP_200_OK, data=data)
