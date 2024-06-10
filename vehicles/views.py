from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Vehicle

def index(request):
    return render(request, 'vehicles/vehicle_listing.html')

def submit_listing(request):
    # Process the form submission here
    # For example, save the listing data to the database
    return HttpResponse("Listing submitted successfully!")

def vehicle_detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    context = {
        'vehicle': vehicle
    }
    return render(request, 'vehicles/vehicle_details.html', context)