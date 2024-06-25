from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.models import Watchlist
from .forms import VehicleForm
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q
from vehicles.models import Vehicle
from bids.models import Bid
from bids.forms import BidForm
from django.utils import timezone
from datetime import timedelta
from .forms import VehicleFilterForm
from .forms import VehicleComparisonForm
from .forms import ContactForm
from .models import Vehicle, ContactMessage

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
            return redirect('my_listings')  # Redirect to a success page
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = VehicleForm()
    return render(request, 'vehicles/vehicle_listing.html', {'form': form})

def vehicle_success(request):
    return render(request, 'vehicles/vehicle_success.html')

def update_bids_table(vehicle):
    if vehicle.first_bid_date:
        auction_ended = timezone.now() > vehicle.first_bid_date + timedelta(days=vehicle.auction_duration_days)
    else:
        auction_ended = False

    if auction_ended:
        # Update bid statuses
        bids = Bid.objects.filter(vehicle=vehicle)
        for bid in bids:
            bid.update_bid_status()

def update_bids_table(vehicle):
    if vehicle.first_bid_date:
        auction_ended = timezone.now() > vehicle.first_bid_date + timedelta(days=vehicle.auction_duration_days)
    else:
        auction_ended = False

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
    vehicle = get_object_or_404(models.Vehicle, pk=vehicle_id)
    highest_bid = Bid.objects.filter(vehicle=vehicle).order_by('-amount').first()
    highest_bid_amount = highest_bid.amount if highest_bid else vehicle.price

    bid_increments = [highest_bid_amount + i * 50000 for i in range(1, 4)]

    auction_ended = False
    remaining_time = None

    if vehicle.first_bid_date:
        auction_end_time = vehicle.first_bid_date + timedelta(days=vehicle.auction_duration_days)
        auction_ended = timezone.now() > auction_end_time
        if not auction_ended:
            remaining_time = auction_end_time - timezone.now()

    total_bids = Bid.objects.filter(vehicle=vehicle).count()

    # Check if the vehicle is in the user's watchlist
    is_in_watchlist = False
    if request.user.is_authenticated:
        is_in_watchlist = Watchlist.objects.filter(user=request.user, vehicle=vehicle).exists()

    context = {
        'is_authenticated': request.user.is_authenticated,
        'vehicle': vehicle,
        'highest_bid': highest_bid_amount,
        'bid_increments': bid_increments,
        'auction_ended': auction_ended,
        'form': BidForm(),
        'is_in_watchlist': is_in_watchlist,
        'total_bids': total_bids,
        'remaining_time': remaining_time.total_seconds() if remaining_time else None,
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
                # Ensure expiry_date is set before saving
                if not bid.expiry_date:
                    if vehicle.first_bid_date:
                        bid.expiry_date = vehicle.first_bid_date + timedelta(days=vehicle.auction_duration_days)
                    else:
                        bid.expiry_date = timezone.now() + timedelta(days=vehicle.auction_duration_days)

                if total_bids == 0 or (total_bids > 0 and not auction_ended and timezone.now() < bid.expiry_date):
                    bid.save()

                    # Update first_bid_date if it's the first bid
                    if not vehicle.first_bid_date:
                        vehicle.first_bid_date = timezone.now()
                        vehicle.save()

                    if auction_ended:
                        update_bids_table(vehicle)

                    return redirect('vehicle_detail', vehicle_id=vehicle.id)
                else:
                    # Handle case where auction has ended or expiry date passed
                    # You can add an error message to the form or display it in the template
                    form.add_error(None, "Bidding is not allowed at this time.")

            context['form'] = form
    else:
        # Create an empty form for GET requests
        context['form'] = BidForm()

    return render(request, 'vehicles/vehicle_details.html', context)

def update_expired_bids():

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
    # Retrieve all vehicles
    cars = models.Vehicle.objects.all()

    # Update expired bids
    update_expired_bids()

    # Retrieve the latest 5 testimonials
    testimonials = ContactMessage.objects.order_by('-timestamp')[:5]

    # Combine all context data
    context = {
        'cars': cars,
        'testimonials': testimonials,
        # Add more context data as needed
    }

    # Render the template with the context data
    return render(request, 'vehicles/home.html', context)


@login_required
def watchlist_view(request):
    watchlist_items = Watchlist.objects.filter(user=request.user).select_related('vehicle')
    context = {
        'watchlist_items': watchlist_items
    }
    return render(request, 'user/watchlist.html', context)

# @login_required
# def vehicle_listing_view(request):
#     # Logic to fetch data for user's bids if needed
#     return render(request, 'vehicles/vehicle_listing.html')

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

@login_required
def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, seller=request.user)
        if form.is_valid():
            form.save()
            return redirect('my_listings')  # Replace 'success_url' with the actual URL name or path
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
    vehicles = models.Vehicle.objects.all()

    context = {
        'vehicles': vehicles,
    }
    return render(request, 'vehicles/compare.html', context)

def filter(request):
    # Fetch all vehicles initially to populate filter options
    vehicles = models.Vehicle.objects.all()

    context = {
        'vehicles': vehicles
    }
    return render(request, 'vehicles/filter_vehicles.html', context)

def filter_vehicles(request):
    form = VehicleFilterForm(request.GET)
    vehicles = models.Vehicle.objects.all()

    if form.is_valid():
        if form.cleaned_data['make']:
            vehicles = vehicles.filter(make=form.cleaned_data['make'])
        if form.cleaned_data['year_min'] is not None:
            vehicles = vehicles.filter(year__gte=form.cleaned_data['year_min'])
        if form.cleaned_data['year_max'] is not None:
            vehicles = vehicles.filter(year__lte=form.cleaned_data['year_max'])
        if form.cleaned_data['body_type']:
            vehicles = vehicles.filter(body_type=form.cleaned_data['body_type'])
        if form.cleaned_data['color']:
            vehicles = vehicles.filter(color__icontains=form.cleaned_data['color'])

        if form.cleaned_data['price_min'] is not None:
            vehicles = vehicles.filter(price__gte=form.cleaned_data['price_min'])
        if form.cleaned_data['price_max'] is not None:
            vehicles = vehicles.filter(price__lte=form.cleaned_data['price_max'])

        if form.cleaned_data['mileage_min'] is not None:
            vehicles = vehicles.filter(mileage__gte=form.cleaned_data['mileage_min'])
        if form.cleaned_data['mileage_max'] is not None:
            vehicles = vehicles.filter(mileage__lte=form.cleaned_data['mileage_max'])

        if form.cleaned_data['engine_capacity_min'] is not None:
            vehicles = vehicles.filter(engine_capacity__gte=form.cleaned_data['engine_capacity_min'])
        if form.cleaned_data['engine_capacity_max'] is not None:
            vehicles = vehicles.filter(engine_capacity__lte=form.cleaned_data['engine_capacity_max'])

        if form.cleaned_data['transmission_type']:
            vehicles = vehicles.filter(transmission_type=form.cleaned_data['transmission_type'])
        if form.cleaned_data['fuel_type']:
            vehicles = vehicles.filter(fuel_type=form.cleaned_data['fuel_type'])
        if form.cleaned_data['engine_type']:
            vehicles = vehicles.filter(engine_type=form.cleaned_data['engine_type'])

        if form.cleaned_data['abs_breaks']:
            vehicles = vehicles.filter(abs_breaks=form.cleaned_data['abs_breaks'])
        if form.cleaned_data['alloy_wheels']:
            vehicles = vehicles.filter(alloy_wheels=form.cleaned_data['alloy_wheels'])
        if form.cleaned_data['airbags']:
            vehicles = vehicles.filter(airbags=form.cleaned_data['airbags'])
        if form.cleaned_data['air_conditioning']:
            vehicles = vehicles.filter(air_conditioning=form.cleaned_data['air_conditioning'])
        if form.cleaned_data['power_steering']:
            vehicles = vehicles.filter(power_steering=form.cleaned_data['power_steering'])
        if form.cleaned_data['power_windows']:
            vehicles = vehicles.filter(power_windows=form.cleaned_data['power_windows'])
        if form.cleaned_data['central_locking']:
            vehicles = vehicles.filter(central_locking=form.cleaned_data['central_locking'])
        if form.cleaned_data['reverse_camera']:
            vehicles = vehicles.filter(reverse_camera=form.cleaned_data['reverse_camera'])
        if form.cleaned_data['sunroof']:
            vehicles = vehicles.filter(sunroof=form.cleaned_data['sunroof'])
        if form.cleaned_data['leather_seats']:
            vehicles = vehicles.filter(leather_seats=form.cleaned_data['leather_seats'])

    return render(request, 'vehicles/filter_vehicles.html', {'form': form, 'vehicles': vehicles})


def all_listings(request):
    # Initial queryset of all vehicles
    vehicles = models.Vehicle.objects.all()

    # Handling search functionality
    query = request.GET.get('q')
    if query:
        vehicles = vehicles.filter(
            Q(model__icontains=query) | Q(description__icontains=query)
        )

    # Filter by price range if min_price and max_price are provided in query parameters
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price and max_price:
        vehicles = vehicles.filter(price__gte=min_price, price__lte=max_price)

    context = {
        'cars': vehicles,  # Renamed 'vehicles' to 'cars' to match your template variable
    }
    return render(request, 'vehicles/all_listings.html', context)

def search_listings(request):
    query = request.GET.get('q')
    all_listings = Listing.objects.filter(title__icontains=query)  # Adjust filtering as per your Listing model fields

    context = {
        'all_listings': all_listings
    }
    return render(request, 'vehicles/all_listings.html', context)

def compare_vehicles(request):
    form = VehicleComparisonForm(request.POST or None)
    compared_data = None
    vehicle1 = vehicle2 = None

    if request.method == 'POST' and form.is_valid():
        vehicle1 = form.cleaned_data['vehicle1']
        vehicle2 = form.cleaned_data['vehicle2']

        # Prepare data for comparison
        excluded_fields = ['id', 'picture', 'picture2', 'picture3', 'description', 'posted_date']
        compared_data = []
        for field in vehicle1._meta.fields:
            if field.name not in excluded_fields:
                field_name = field.verbose_name.capitalize()
                value1 = getattr(vehicle1, field.name)
                value2 = getattr(vehicle2, field.name)

                # Format price in LKR with commas
                if field.name == 'price':
                    value1 = f"LKR {value1:,.2f}"
                    value2 = f"LKR {value2:,.2f}"

                compared_data.append((field_name, value1, value2))

    context = {
        'form': form,
        'vehicle1': vehicle1,
        'vehicle2': vehicle2,
        'compared_data': compared_data,
    }
    return render(request, 'vehicles/compare_vehicles.html', context)


from django.shortcuts import render, get_object_or_404
from . import models

from django.shortcuts import render, get_object_or_404
from user.models import User
from .models import Vehicle

def seller_listings(request):
    seller_id = request.GET.get('seller_id')

    # Debugging print statement
    print(f"Fetching seller with ID: {seller_id}")

    seller = get_object_or_404(User, id=seller_id)
    listings = Vehicle.objects.filter(seller=seller)

    context = {
        'seller': seller,
        'listings': listings
    }

    return render(request, 'vehicles/seller_listings.html', context)


@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')  # Redirect to homepage to see the testimonial
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'vehicles/contact.html', context)






