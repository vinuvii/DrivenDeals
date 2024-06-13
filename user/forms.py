from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email_address', 'mobile_number', 'postal_code', 'trading_address']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    mobile_number = forms.CharField(max_length=15, required=False)
    postal_code = forms.CharField(max_length=10, required=False)
    trading_address = forms.CharField(max_length=255, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'mobile_number', 'postal_code', 'trading_address']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            UserProfile.objects.update_or_create(
                user=user,
                defaults={
                    'email_address': self.cleaned_data['email'],
                    'mobile_number': self.cleaned_data['mobile_number'],
                    'postal_code': self.cleaned_data['postal_code'],
                    'trading_address': self.cleaned_data['trading_address']
                }
            )
        return user