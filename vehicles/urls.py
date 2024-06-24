from django.urls import path
from . import views
from .views import filter_vehicles


urlpatterns = [
    path('', views.home, name='home'),
    path('submit-form/', views.submit_form, name='submit_form'),
    path('vehicle-listing/', views.add_vehicle, name='vehicle_listing'),
    path('watchlist/', views.watchlist_view, name='watchlist'),

    path('index/', views.index, name='index'),
    path('vehicle_detail/<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),
    path('list/', views.list_vehicle, name='list_vehicle'),
    path('success/', views.vehicle_success, name='vehicle_success'),
    path('submit/', views.list_vehicle, name='submit_listing'),


    path('about/', views.about, name='about'),
    path('blog1/', views.blog1, name='blog1'),
    path('blog2/', views.blog2, name='blog2'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('compare/', views.compare_vehicles, name='compare_vehicles'),
    path('filter/', filter_vehicles, name='filter_vehicles'),
    path('all-listings/', views.all_listings, name='all_listings'),
    path('all_listings/search/', views.search_listings, name='search_listings'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),  # Optionally define a success page
    path('seller_listings/', views.seller_listings, name='seller_listings'),

]