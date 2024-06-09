from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('favourites/', views.favourites, name='favourites'),
    path('my_listings/', views.my_listings, name='my_listings'),
    path('logout/', views.logout, name='logout'),
]