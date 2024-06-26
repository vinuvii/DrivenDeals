from django.urls import path
from . import views

urlpatterns = [
    path('my_listings/', views.my_listings_view, name='my_listings'),
    path('my_bids/', views.my_bids_view, name='my_bids'),

    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('redirect-to-login/', views.redirect_to_login, name='redirect_to_login'),

    path('', views.index, name='index'),

    path('add_to_watchlist/<int:vehicle_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('remove_from_watchlist/<int:vehicle_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('toggle_watchlist/<int:vehicle_id>/', views.toggle_watchlist, name='toggle_watchlist'),


    path('logout/confirmation/', views.logout_confirmation, name='logout_confirmation'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.custom_login, name='login'),

    path('listing/<int:pk>/', views.listing_detail, name='listing_detail'),
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
]