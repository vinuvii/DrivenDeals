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


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control'
    }))


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100, required=True, help_text='Enter your first name')
    last_name = forms.CharField(max_length=100, required=True, help_text='Enter your last name')
    mobile_number = forms.CharField(max_length=20, required=True, help_text='Enter your contact number')
    trading_address = forms.CharField(max_length=255, required=True, help_text='Enter your trading address')
    postal_code = forms.CharField(max_length=20, required=True, help_text='Enter your postal code')

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'mobile_number', 'trading_address', 'postal_code']
