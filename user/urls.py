from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('add_to_watchlist/<int:item_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('remove_from_watchlist/<int:item_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('my-listings/', views.my_listings, name='my_listings'),
    path('my-bids/', views.my_bids, name='my_bids'),
    path('logout/confirmation/', views.logout_confirmation, name='logout_confirmation'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.custom_login, name='login'),
    path('listing/<int:pk>/', views.listing_detail, name='listing_detail'),
]