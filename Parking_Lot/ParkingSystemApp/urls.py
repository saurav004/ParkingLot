from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('owner_api/', views.OwnerApi.as_view(), name='owner_list'),
    path('owner_api/<int:pk>', views.OwnerApi.as_view(), name='owner_detail'),
    path('parking_api/', views.ParkingApi.as_view(), name='parking_list'),
    path('parking_api/<int:pk>', views.ParkingApi.as_view(), name='parking_detail'),
    path('vehicle_api/', views.VehicleApi.as_view(), name='vehicle_list'),
    path('vehicle_api/<int:pk>', views.VehicleApi.as_view(), name='vehicle_detail'),
    path('police_or_security/', views.PoliceOrSecurityApi.as_view(), name='police_or_security_list'),
    path('police_or_security/<int:pk>', views.PoliceOrSecurityApi.as_view(), name='police_or_security_detail'),
    path('valet_api/', views.ValetApi.as_view(), name='valet_list'),
    path('valet_api/<int:pk>', views.ValetApi.as_view(), name='valet_detail'),
    path('slot_api/', views.SlotApi.as_view(), name='slot_list'),
    path('slot_api/<int:pk>', views.SlotApi.as_view(), name='slot_detail'),
    path('driver_api/', views.DriverApi.as_view(), name='driver_list'),
    path('find_my_car_api/', views.find_my_car_api, name='find_car'),
    path('driver_api/<int:pk>', views.DriverApi.as_view(), name='driver_detail'),
    path('park_api/', views.park_my_car, name='park'),
    path('unpark_api', views.unpark_my_car, name='unpark'),

]
