from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('signup/', views.signup_view, name='signup'),
    path('submit-form/', views.submit_form, name='submit_form'),
    path('vehicle-listing/', views.add_vehicle, name='vehicle_listing'),
    path('watchlist/', views.watchlist_view, name='watchlist'),
    path('my_listings/', views.my_listings_view, name='my_listings'),
    path('my_bids/', views.my_bids_view, name='my_bids'),
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
    path('index/', views.index, name='index'),  # Example path for index
    path('vehicle_detail/<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),
    path('list/', views.list_vehicle, name='list_vehicle'),
    path('success/', views.vehicle_success, name='vehicle_success'),
    path('submit/', views.list_vehicle, name='submit_listing'),  # Example path for submitting vehicles


    path('about/', views.about, name='about'),
    path('blog1/', views.blog1, name='blog1'),
    path('blog2/', views.blog2, name='blog2'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('compare/', views.compare, name='compare'),
    path('filter/', views.filter, name='filter'),
]