from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('watchlist/', views.watchlist, name='watchlist'),  # Updated this line
    path('my-listings/', views.my_listings, name='my_listings'),
    path('my-bids/', views.my_bids, name='my_bids'),
    path('logout/confirmation/', views.logout_confirmation, name='logout_confirmation'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.custom_login, name='login'),
]