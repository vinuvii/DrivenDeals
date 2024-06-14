from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vehicle-listing/', views.vehicle_listing_view, name='vehicle_listing'),
    path('watchlist/', views.watchlist_view, name='watchlist'),
    path('my_listings/', views.my_listings_view, name='my_listings'),
    path('my_bids/', views.my_bids_view, name='my_bids'),
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
    path('index/', views.index, name='index'),  # Example path for index
    path('vehicle_detail/<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),
    path('list/', views.list_vehicle, name='list_vehicle'),
    path('success/', views.vehicle_success, name='vehicle_success'),
    path('submit/', views.list_vehicle, name='submit_listing'),  # Example path for submitting vehicles
]