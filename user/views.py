from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views

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
            messages.success(request, 'Your profile was updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'user/edit_profile.html', {'form': form})

@login_required
def favourites(request):
    return render(request, 'user/favourites.html')

@login_required
def my_listings(request):
    return render(request, 'user/my_listings.html')

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


