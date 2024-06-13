from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from .models import UserProfile, Listing
from .models import WatchlistItem
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'user/profile.html')

@login_required
def profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'user/profile.html', {'user_profile': user_profile})

@login_required
def edit_profile(request):
    if request.user.is_authenticated:  # Ensure user is authenticated
        user_profile = get_object_or_404(UserProfile, user=request.user)
        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=user_profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile was updated successfully!')
                return redirect('profile')
        else:
            form = UserProfileForm(instance=user_profile)
        return render(request, 'user/edit_profile.html', {'form': form})
    else:
        return redirect('login')  # Redirect to login if user is not authenticated


@login_required
def watchlist(request):
    watchlist_items = WatchlistItem.objects.filter(user=request.user)
    return render(request, 'user/watchlist.html', {'watchlist_items': watchlist_items})

@login_required
def add_to_watchlist(request, item_id):
    watchlist_item = WatchlistItem(user=request.user, item_id=item_id)
    watchlist_item.save()
    return redirect('watchlist')

@login_required
def remove_from_watchlist(request, item_id):
    WatchlistItem.objects.filter(user=request.user, item_id=item_id).delete()
    return redirect('watchlist')

@login_required
def my_listings(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    listings = Listing.objects.filter(user=request.user)  # Fetch the user's listings
    return render(request, 'user/my_listings.html', {'listings': listings})

@login_required
def my_bids(request):
    return render(request, 'user/my_bids.html')

@login_required
def logout_confirmation(request):
    return render(request, 'user/logout_confirmation.html')

def logout_view(request):
    auth_logout(request)  # Use the auth_logout function from django.contrib.auth
    return redirect('login')

def custom_login(request):
    return auth_views.LoginView.as_view(template_name='user/login.html')(request)

@login_required
def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'user/listing_detail.html', {'listing': listing})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Authenticate and login user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            # Redirect to success page or homepage
            return redirect('registration_success')  # Replace 'home' with your homepage URL name
    else:
        form = UserRegistrationForm()
    return render(request, 'user/register.html', {'form': form})


