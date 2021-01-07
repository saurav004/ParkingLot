from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('owner_api/', views.OwnerApi.as_view(), name='owner_list'),
    path('parking_api/', views.ParkingApi.as_view(), name='parking_list'),
    path('vehicle_api/', views.VehicleApi.as_view(), name='vehicle_list'),
    path('police_or_security/', views.PoliceOrSecurityApi.as_view(), name='police_or_security_list'),
    path('valet_api/', views.ValetApi.as_view(), name='valet_list'),
    path('slot_api/', views.SlotApi.as_view(), name='slot_list'),
    path('driver_api/', views.DriverApi.as_view(), name='driver_list'),
    path('find_my_car_api/', views.find_my_car_api, name='find_car'),
    path('park_api/', views.park_my_car, name='park'),
    path('unpark_api/', views.unpark_my_car, name='unpark'),
    path('vehicle_location_api/', views.get_vehicle_location_info, name='location_info'),
    path('vehicle_info_for_investigation/', views.get_location_number_parking_attendant_info,
         name='vehicle_investigation'),
    path('vehicle_info/', views.get_vehicle_details, name='vehicle_info'),
    path('vehicle_info_parked_earlier/', views.get_vehicle_info_parked_before_time_given,
         name='vehicle_info_back_in_time'),
    path('all_vehicle_info_in_the_lot/', views.get_info_of_all_vehicles_parked_in_the_lot,
         name='all_vehicle_info_in_the_lot'),
]
