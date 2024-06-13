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
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

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