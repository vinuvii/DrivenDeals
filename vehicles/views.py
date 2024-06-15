from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages  # Import messages
from django.contrib.auth.decorators import login_required
from .models import Vehicle
from .forms import VehicleForm
from django.urls import reverse

def index(request):
    return render(request, 'vehicles/vehicle_listing.html')

@login_required
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
        'is_authenticated': request.user.is_authenticated,
        'vehicle': vehicle,
    }

    if request.method == 'POST' and not request.user.is_authenticated:
        # If it's a POST request and user is not authenticated, redirect to login
        login_url = reverse('login')  # Assuming 'login' is your login URL name
        return redirect(f"{login_url}?next={request.path}")

    return render(request, 'vehicles/vehicle_details.html', context)

def home(request):
    cars = Vehicle.objects.all()  # Assuming you have a Vehicle model
    return render(request, 'vehicles/home.html', {'cars': cars})


@login_required
def watchlist_view(request):
    # Logic to fetch data for watchlist if needed
    return render(request, 'user/watchlist.html')

@login_required
def my_listings_view(request):
    # Logic to fetch data for user's listings if needed
    return render(request, 'user/my_listings.html')

@login_required
def my_bids_view(request):
    # Logic to fetch data for user's bids if needed
    return render(request, 'user/my_bids.html')

@login_required
def edit_profile_view(request):
    # Logic to fetch data for user's bids if needed
    return render(request, 'user/edit_profile.html')

@login_required
def vehicle_listing_view(request):
    # Logic to fetch data for user's bids if needed
    return render(request, 'vehicles/vehicle_listing.html')

def about(request):
    return render(request, 'vehicles/about.html')

def blog1(request):
    return render(request, 'vehicles/blog1.html')

def blog2(request):
    return render(request, 'vehicles/blog2.html')

def services(request):
    return render(request, 'vehicles/services.html')

