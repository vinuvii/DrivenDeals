from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'vehicles/vehicle_listing.html')

def submit_listing(request):
    # Process the form submission here
    # For example, save the listing data to the database
    return HttpResponse("Listing submitted successfully!")
