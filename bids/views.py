from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Bid
from vehicles.models import Vehicle
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import BidForm
from payments.views import make_payment

@login_required
def place_bid(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)

    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            bid_amount = form.cleaned_data['bid_amount']

            # Simulate payment (amount can be a fixed amount or calculated)
            amount_to_charge = bid_amount  # Example: charge the bid amount
            response = make_payment(request, amount_to_charge)

            # If payment is successful, proceed to save the bid
            if response.status_code == 200:  # Assuming make_payment returns a HttpResponse
                # Check if it's the first bid on this vehicle
                if not vehicle.first_bid_date:
                    vehicle.first_bid_date = timezone.now()  # Update first_bid_date
                    vehicle.save()

                # Create the bid
                Bid.objects.create(car=vehicle, bidder=request.user.userprofile, bid_amount=bid_amount)
                return redirect('bid_success')  # Redirect to a success page or vehicle detail page
            else:
                # Handle payment failure scenario
                return HttpResponse("Payment failed. Please try again.")

    # Redirect to vehicle detail page if POST method is not used
    return redirect('vehicle_detail', vehicle_id=vehicle_id)

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
#
# def vehicle_detail(request, vehicle_id):
#     vehicle = get_object_or_404(Vehicle, id=vehicle_id)
#     context = {
#         'vehicle': vehicle,
#     }
#     return render(request, 'vehicle_detail.html', context)

from django.utils import timezone
from datetime import timedelta
from .models import Bid

def update_expired_bids():
    """
    Update bid statuses for expired bids.
    For each vehicle, mark the highest bid as accepted and others as rejected.
    """
    # Get all bids with expiry date less than or equal to current time
    expired_bids = Bid.objects.filter(expiry_date__lte=timezone.now())

    for bid in expired_bids:
        # Get all bids for the current vehicle
        all_bids = Bid.objects.filter(vehicle=bid.vehicle).order_by('-amount')

        if all_bids.exists():
            highest_bid = all_bids.first()  # Highest bid is the first bid in descending order by amount

            for single_bid in all_bids:
                if single_bid == highest_bid:
                    single_bid.bid_status = Bid.BID_STATUS_ACCEPTED
                else:
                    single_bid.bid_status = Bid.BID_STATUS_REJECTED
                single_bid.save()