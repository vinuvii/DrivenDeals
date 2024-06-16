from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Bid
from vehicles.models import Vehicle
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import BidForm

@login_required
def place_bid(request):
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            car_id = form.cleaned_data['car_id']
            bid_amount = form.cleaned_data['bid_amount']
            vehicle = get_object_or_404(Vehicle, pk=car_id)
            Bid.objects.create(car=vehicle, bidder=request.user.userprofile, bid_amount=bid_amount)
            return redirect('bid_success')  # Redirect to a success page or vehicle detail page
    return redirect('vehicle_detail', vehicle_id=request.POST.get('car_id'))

def determine_bid_status(bid):
    if bid.expiry_date and bid.expiry_date <= timezone.now():
        bid.bid_status = 'EXPIRED'
        bid.save()
        highest_bid = bid.car.bids.exclude(id=bid.id).order_by('-bid_amount').first()
        if highest_bid:
            bid.car.owner = highest_bid.bidder
            bid.car.save()
            return f"Car sold to {highest_bid.bidder} for {highest_bid.bid_amount}"
        else:
            return "No bids received for the car"
    else:
        return "Bid is still active"

def vehicle_detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    context = {
        'vehicle': vehicle,
    }
    return render(request, 'vehicle_detail.html', context)

from django.utils import timezone
from datetime import timedelta
from .models import Bid

def update_expired_bids():
    """
    Update bid statuses for expired bids.
    For each vehicle, classify bids, mark the highest bid as accepted, and others as rejected.
    """
    # Get all vehicles with expired bids
    expired_vehicles = Bid.objects.filter(expiry_date__lte=timezone.now())

    for vehicle in expired_vehicles:
        # Get all bids for the current vehicle
        bids = Bid.objects.filter(vehicle=vehicle).order_by('-amount')

        if bids.exists():
            highest_bid = bids.first()  # Highest bid is the first bid in descending order by amount

            for bid in bids:
                if bid == highest_bid:
                    bid.bid_status = Bid.BID_STATUS_ACCEPTED
                else:
                    bid.bid_status = Bid.BID_STATUS_REJECTED
                bid.save()
