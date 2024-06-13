from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vehicle_detail/<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),
    #path('submit/', views.submit_listing, name='submit_listing'),
    #path('vehicle_detail/<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),
    path('list/', views.list_vehicle, name='list_vehicle'),
    path('success/', views.vehicle_success, name='vehicle_success'),
    path('submit/', views.list_vehicle, name='list_vehicle'),
]