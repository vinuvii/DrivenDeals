from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

from bids.models import Bid
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Listing
from .models import Watchlist
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from vehicles.models import Vehicle
from django.contrib.auth.decorators import login_required
from .models import UserWatchlistItem

def index(request):
    return render(request, 'user/profile.html')

@login_required
def profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'user/profile.html', {'user_profile': user_profile})

@login_required
def edit_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'user/edit_profile.html', {'form': form})

# @login_required
# def my_watchlist(request):
#     watchlist_items = UserWatchlistItem.objects.filter(user=request.user).select_related('vehicle')
#     context = {'listings': [item.vehicle for item in watchlist_items]}
#     return render(request, 'user/watchlist.html', context)
#
# @login_required
# def add_to_watchlist(request, vehicle_id):
#     vehicle = get_object_or_404(Vehicle, id=vehicle_id)
#     Watchlist.objects.get_or_create(user=request.user, vehicle=vehicle)
#     return redirect('my_watchlist')
#
# @login_required
# def remove_from_watchlist(request, vehicle_id):
#     vehicle = get_object_or_404(Vehicle, id=vehicle_id)
#     Watchlist.objects.filter(user=request.user, vehicle=vehicle).delete()
#       return redirect('my_watchlist')
#
# @login_required
# def my_watchlist(request):
#     watchlist_items = Watchlist.objects.filter(user=request.user).select_related('vehicle')
#     context = {'listings': [item.vehicle for item in watchlist_items]}
#     return render(request, 'watchlist.html', context)

@login_required
def my_bids(request):
    return render(request, 'user/my_bids.html')

@login_required
def logout_confirmation(request):
    return render(request, 'user/logout_confirmation.html')


def custom_login(request):
    return auth_views.LoginView.as_view(template_name='user/login_copy.html')(request)

@login_required
def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'user/listing_detail.html', {'listing': listing})

def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def redirect_to_login(request):
    if not request.user.is_authenticated:
        return redirect(f"{reverse_lazy('login')}?next={request.path}")
    return redirect(request.path)

from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserLoginForm

from django.contrib.auth import authenticate, login
from .forms import UserLoginForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

def login_view(request):
    error_message = None
    next_url = request.POST.get('next') or request.GET.get('next')

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('home')  # Default redirect if no next_url
            else:
                error_message = 'Incorrect email or password'
        else:
            error_message = 'Please enter a valid email and password'
    else:
        form = UserLoginForm()

    return render(request, 'user/login.html', {'form': form, 'error_message': error_message, 'next': next_url})


@login_required
def my_listings_view(request):
    user_id = request.user.id
    debug_info = []  # List to collect debug information

    try:
        vehicles = Vehicle.objects.filter(seller_id=user_id)
        debug_info.append(f"Fetched vehicles: {list(vehicles)}")
        debug_info.append(f"Logged in user id: {user_id}")
    except Vehicle.DoesNotExist:
        debug_info.append("No vehicles found for user")
        vehicles = []

    context = {
        'vehicles': vehicles,
        'debug_info': debug_info
    }
    return render(request, 'user/my_listings.html', context)

@login_required
def my_bids_view(request):
    user = request.user
    bids = Bid.objects.filter(user=user)

    context = {
        'bids': bids
    }
    return render(request, 'user/my_bids.html', context)



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Watchlist
from vehicles.models import Vehicle
from .forms import UserProfileForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import views as auth_views
from bids.models import Bid
from .models import UserProfile

@login_required
@require_POST
def add_to_watchlist(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    Watchlist.objects.get_or_create(user=request.user, vehicle=vehicle)
    return redirect('watchlist')


@login_required
@require_POST
def remove_from_watchlist(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    watchlist_item = Watchlist.objects.filter(user=request.user, vehicle=vehicle)

    if watchlist_item.exists():
        watchlist_item.delete()
        # Return JSON response indicating successful removal
        return JsonResponse({'removed': True})
    else:
        # Return JSON response indicating failure (though this should not normally happen if proper checks are in place)
        return JsonResponse({'removed': False, 'error': 'Item not found in watchlist'}, status=404)

@login_required
@require_POST
def toggle_watchlist(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    watchlist_item, created = Watchlist.objects.get_or_create(user=request.user, vehicle=vehicle)

    if not created:
        watchlist_item.delete()
        return JsonResponse({'added': False})
    else:
        return JsonResponse({'added': True})

