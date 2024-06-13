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
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control'
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control'
    }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control'
    }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control'
    }))
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
        'class': 'form-control'
    }))
    last_name = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Last Name',
        'class': 'form-control'
    }))
    mobile_number = forms.CharField(label='Contact Number', max_length=15, widget=forms.TextInput(attrs={
        'placeholder': 'Contact Number',
        'class': 'form-control'
    }))
    postal_code = forms.CharField(label='Postal Code', max_length=10, widget=forms.TextInput(attrs={
        'placeholder': 'Postal Code',
        'class': 'form-control'
    }))
    trading_address = forms.CharField(label='Trading Address', widget=forms.TextInput(attrs={
        'placeholder': 'Trading Address',
        'class': 'form-control'
    }))