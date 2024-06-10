from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages  # Import messages
from .models import Vehicle
from .forms import VehicleForm

def index(request):
    return render(request, 'vehicles/vehicle_listing.html')

def list_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your vehicle has been listed successfully!')
            return redirect('vehicle_success')  # Redirect to a success page
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = VehicleForm()
    return render(request, 'vehicles/vehicle_listing.html', {'form': form})

def vehicle_success(request):
    return render(request, 'vehicles/vehicle_success.html')

def vehicle_detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    context = {
        'vehicle': vehicle
    }
    return render(request, 'vehicles/vehicle_details.html', context)
