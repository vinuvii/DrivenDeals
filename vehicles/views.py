from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages  # Import messages
from django.contrib.auth.decorators import login_required
from .models import Vehicle
from .forms import VehicleForm
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Vehicle

def index(request):
    return render(request, 'vehicles/vehicle_listing.html')

@login_required
def list_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.seller = request.user
            vehicle.save()
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

from django.shortcuts import render, redirect

@require_POST
def submit_form(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.seller = request.user
            vehicle.save()
            if request.is_ajax():
                return JsonResponse({'status': 'success'})
            else:
                messages.success(request, 'Your vehicle has been listed successfully!')
                return redirect('vehicle_success')
        else:
            if request.is_ajax():
                return JsonResponse({'status': 'error', 'errors': form.errors})
            else:
                messages.error(request, 'Please correct the errors below.')
                return render(request, 'vehicles/vehicle_listing.html', {'form': form})
    else:
        return JsonResponse({'status': 'error', 'errors': 'Invalid request'})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VehicleForm


@login_required
def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, seller=request.user)
        if form.is_valid():
            form.save()
            return redirect('vehicle_success')  # Replace 'success_url' with the actual URL name or path
        else:
            print("Form is invalid")
            print(form.errors)  # Debug: Print form errors to the console
    else:
        form = VehicleForm(seller=request.user)

    return render(request, 'vehicles/vehicle_listing.html', {'form': form})