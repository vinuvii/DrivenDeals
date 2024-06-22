# vehicles/views.py
from django.shortcuts import render

from payments.models import Payment  # Import the Payment model

@login_required
def list_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.seller = request.user

            # Create a pending payment record
            amount_to_charge = 20.00  # Example amount to charge for listing a vehicle
            payment = Payment.objects.create(user=request.user, vehicle=vehicle, amount=amount_to_charge, status='PENDING')

            # Simulate payment
            response = make_payment(request, amount_to_charge)

            if response.status_code == 200:
                payment.status = 'COMPLETED'
                payment.save()

                vehicle.save()
                messages.success(request, 'Your vehicle has been listed successfully!')
                return redirect('vehicle_success')
            else:
                payment.status = 'FAILED'
                payment.save()
                messages.error(request, 'Payment failed. Please try again.')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = VehicleForm()

    return render(request, 'vehicles/vehicle_listing.html', {'form': form})
