from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

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

@login_required
def favourites(request):
    # Implement logic for favourites
    return render(request, 'user/favourites.html')

@login_required
def my_listings(request):
    # Implement logic for my listings
    return render(request, 'user/my_listings.html')

@login_required
def my_bids(request):
    # Implement logic for my listings
    return render(request, 'user/my_bids.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')  # Assuming you have a login view to redirect to
