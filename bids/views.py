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