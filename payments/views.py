# vehicles/views.py
from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.shortcuts import render

from payments.models import Payment  # Import the Payment model
from vehicles.forms import VehicleForm


# vehicles/utils.py

def make_payment(user, amount, vehicle):
    """
    Process payment for vehicle listing.

    Args:
        user: The user making the payment.
        amount: The amount to be paid.
        vehicle: The vehicle being listed.

    Returns:
        bool: True if payment is successful, False otherwise.
    """
    # Here we can use a payment gateway API like Stripe, PayPal, etc.
    # For the sake of this example, let's assume a mock payment processing.

    # Mock payment processing
    try:
        # Simulate payment processing logic
        print(f"Processing payment of {amount} for {user.username}")

        # If payment is successful
        payment_successful = True

        if payment_successful:
            print(f"Payment successful for vehicle: {vehicle}")
            return True
        else:
            print(f"Payment failed for vehicle: {vehicle}")
            return False
    except Exception as e:
        print(f"Payment processing error: {str(e)}")
        return False


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
