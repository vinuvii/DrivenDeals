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
from django.db.models import Q
from vehicles.models import Vehicle
from bids.models import Bid
from bids.forms import BidForm
from django.utils import timezone
from datetime import timedelta

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


def update_bids_table(vehicle):
    auction_ended = timezone.now() > vehicle.posted_date + timedelta(days=7)

    if auction_ended:
        # Update bid statuses
        bids = Bid.objects.filter(vehicle=vehicle)
        for bid in bids:
            bid.update_bid_status()

def update_bids_table(vehicle):
    auction_ended = timezone.now() > vehicle.posted_date + timedelta(days=7)

    if auction_ended:
        # Determine the winning bid
        highest_bid = Bid.objects.filter(vehicle=vehicle).order_by('-amount').first()

        if highest_bid:
            # Update bid statuses
            bids = Bid.objects.filter(vehicle=vehicle)
            for bid in bids:
                if bid == highest_bid:
                    bid.bid_status = Bid.BID_STATUS_ACCEPTED
                else:
                    bid.bid_status = Bid.BID_STATUS_REJECTED
                bid.save()

def vehicle_detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    highest_bid = Bid.objects.filter(vehicle=vehicle).order_by('-amount').first()
    highest_bid_amount = highest_bid.amount if highest_bid else vehicle.price

    bid_increments = [highest_bid_amount + i * 50000 for i in range(1, 4)]

    auction_ended = timezone.now() > vehicle.posted_date + timedelta(days=7)

    context = {
        'is_authenticated': request.user.is_authenticated,
        'vehicle': vehicle,
        'highest_bid': highest_bid_amount,
        'bid_increments': bid_increments,
        'auction_ended': auction_ended,
        'form': BidForm(),
    }

    if request.method == 'POST':
        if not request.user.is_authenticated:
            # If it's a POST request and the user is not authenticated, redirect to login
            login_url = reverse('login')  # Assuming 'login' is your login URL name
            return redirect(f"{login_url}?next={request.path}")
        else:
            # Handle the bid submission
            form = BidForm(request.POST)
            if form.is_valid():
                bid = form.save(commit=False)
                bid.user = request.user
                bid.vehicle = vehicle
                bid.save()

                if auction_ended:
                    update_bids_table(vehicle)

                return redirect('vehicle_detail', vehicle_id=vehicle.id)
            else:
                context['form'] = form
    else:
        # Create an empty form for GET requests
        context['form'] = BidForm()

    return render(request, 'vehicles/vehicle_details.html', context)

def update_expired_bids():
    """
    Update bid statuses for expired bids.
    For each vehicle, classify bids, mark the highest bid as accepted, and others as rejected.
    """
    # Get all bids with expired expiry_date
    expired_bids = Bid.objects.filter(expiry_date__lte=timezone.now())

    for bid in expired_bids:
        # Get all bids for the current vehicle
        vehicle_bids = Bid.objects.filter(vehicle=bid.vehicle).order_by('-amount')

        if vehicle_bids.exists():
            highest_bid = vehicle_bids.first()  # Highest bid is the first bid in descending order by amount

            for vehicle_bid in vehicle_bids:
                if vehicle_bid == highest_bid:
                    vehicle_bid.bid_status = Bid.BID_STATUS_ACCEPTED
                else:
                    vehicle_bid.bid_status = Bid.BID_STATUS_REJECTED
                vehicle_bid.save()
                
def home(request):
    cars = Vehicle.objects.all()
    update_expired_bids()
    context = {
        'cars': cars,
        # Add more context data as needed
    }
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






def about(request):
    return render(request, 'vehicles/about.html')

def blog1(request):
    return render(request, 'vehicles/blog1.html')

def blog2(request):
    return render(request, 'vehicles/blog2.html')

def services(request):
    return render(request, 'vehicles/services.html')

def contact(request):
    return render(request, 'vehicles/contact.html')

def compare(request):
    # Fetch all vehicles from the database
    vehicles = Vehicle.objects.all()

    context = {
        'vehicles': vehicles,
    }
    return render(request, 'vehicles/compare.html', context)

def filter(request):
    # Fetch all vehicles initially to populate filter options
    vehicles = Vehicle.objects.all()

    context = {
        'vehicles': vehicles
    }
    return render(request, 'vehicles/filter.html', context)

def filter_vehicles(request):
    make = request.GET.get('make')
    # Add more filters as needed (e.g., model, year, transmission_type)

    # Filtering based on selected criteria
    filtered_vehicles = Vehicle.objects.all()
    if make:
        filtered_vehicles = filtered_vehicles.filter(make=make)
    # Add more filtering conditions as per other criteria

    # Serialize vehicles and their price (assuming price is a field in Vehicle model)
    filtered_data = []
    for vehicle in filtered_vehicles:
        vehicle_data = {
            'make': vehicle.make,
            'model': vehicle.model,
            'year': vehicle.year,
            'body_type': vehicle.body_type,
            'no_of_seats': vehicle.no_of_seats,
            'transmission_type': vehicle.transmission_type,
            'fuel_type': vehicle.fuel_type,
            'engine_capacity': vehicle.engine_capacity,
            'engine_type': vehicle.engine_type,
            'abs_breaks': vehicle.abs_breaks,
            'alloy_wheels': vehicle.alloy_wheels,
            'airbags': vehicle.airbags,
            'air_conditioning': vehicle.air_conditioning,
            'power_steering': vehicle.power_steering,
            'power_windows': vehicle.power_windows,
            'central_locking': vehicle.central_locking,
            'reverse_camera': vehicle.reverse_camera,
            'leather_seats': vehicle.leather_seats,
            'sunroof': vehicle.sunroof,
            'price': vehicle.price  # Include price field
            # Add more fields as needed
        }
        filtered_data.append(vehicle_data)

    return JsonResponse(filtered_data, safe=False)


def all_listings(request):
    cars = Vehicle.objects.all()

    # Handling search functionality
    query = request.GET.get('q')
    if query:
        cars = cars.filter(
            Q(model__icontains=query) | Q(description__icontains=query)
        )

    context = {
        'cars': cars
    }
    return render(request, 'vehicles/all_listings.html', context)

def search_listings(request):
    query = request.GET.get('q')
    all_listings = Listing.objects.filter(title__icontains=query)  # Adjust filtering as per your Listing model fields

    context = {
        'all_listings': all_listings
    }
    return render(request, 'vehicles/all_listings.html', context)