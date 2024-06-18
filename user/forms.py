from django import forms
from django.contrib.auth.forms import UserCreationForm
#from .models import UserProfile
from django.contrib.auth.models import User

#
# class UserProfileForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#
#     class Meta:
#         model = UserProfile
#         fields = ['mobile_number', 'postal_code', 'trading_address']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Populate the user fields from the related User instance
#         if self.instance and self.instance.user:
#             self.fields['first_name'].initial = self.instance.user.first_name
#             self.fields['last_name'].initial = self.instance.user.last_name
#             self.fields['email'].initial = self.instance.user.email
#
#     def save(self, commit=True):
#         user = self.instance.user
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#             self.instance.save()
#         return self.instance


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control'
    }))


from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name', 'mobile_number', 'postal_code', 'trading_address')

class UserRegistrationForm(CustomUserCreationForm):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Username',
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

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'mobile_number', 'postal_code', 'trading_address']