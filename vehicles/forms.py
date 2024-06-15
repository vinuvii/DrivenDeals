from django import forms
from django.contrib.auth import get_user_model
from .models import Vehicle

User = get_user_model()

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.seller = kwargs.pop('seller', None)
        super().__init__(*args, **kwargs)
        # Example: Customize widgets or add additional attributes if needed
        self.fields['make'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter make'})
        self.fields['model'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter model'})
        self.fields['year'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter year'})
        self.fields['body_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['color'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter color'})
        self.fields['mileage'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter mileage'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter price'})
        self.fields['transmission_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['fuel_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['engine_capacity'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter engine capacity'})
        self.fields['engine_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['no_of_seats'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter number of seats'})
        self.fields['abs_breaks'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['alloy_wheels'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['airbags'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['air_conditioning'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['power_steering'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['power_windows'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['central_locking'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['reverse_camera'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['sunroof'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['leather_seats'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['picture'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['picture2'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['picture3'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': 4, 'placeholder': 'Enter description'})

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.seller:
            instance.seller = self.seller
        if commit:
            instance.save()
        return instance
