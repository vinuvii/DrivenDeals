from django.urls import path
from . import views

urlpatterns = [
    path('place_bid/', views.place_bid, name='place_bid'),
]