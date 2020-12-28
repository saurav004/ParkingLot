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
    path('slot_api/', views.SlotApi.as_view(), name='slot_list'),
    path('slot_api/<int:pk>', views.SlotApi.as_view(), name='slot_detail'),
]
