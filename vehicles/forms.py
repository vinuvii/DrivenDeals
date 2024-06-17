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


class VehicleFilterForm(forms.Form):
    MANUFACTURER_CHOICES = [
        ('', 'Any'),
        ('Audi', 'Audi'),
        ('BMW', 'BMW'),
        ('Chevrolet', 'Chevrolet'),
        ('Ferrari', 'Ferrari'),
        ('Ford', 'Ford'),
        ('Honda', 'Honda'),
        ('Hyundai', 'Hyundai'),
        ('Jaguar', 'Jaguar'),
        ('Kia', 'Kia'),
        ('Lamborghini', 'Lamborghini'),
        ('Mahindra', 'Mahindra'),
        ('Mazda', 'Mazda'),
        ('McLaren', 'McLaren'),
        ('Mercedes-Benz', 'Mercedes-Benz'),
        ('Mitsubishi', 'Mitsubishi'),
        ('Nissan', 'Nissan'),
        ('Peugeot', 'Peugeot'),
        ('Perodua', 'Perodua'),
        ('Porsche', 'Porsche'),
        ('Renault', 'Renault'),
        ('Rolls-Royce', 'Rolls-Royce'),
        ('Suzuki', 'Suzuki'),
        ('Tata Motors', 'Tata Motors'),
        ('Tesla', 'Tesla'),
        ('Toyota', 'Toyota'),
        ('Volkswagen', 'Volkswagen'),
        ('Volvo', 'Volvo'),
        ('other', 'Other'),
    ]

    BODYTYPE_CHOICES = [
        ('', 'Any'),
        ('motorbike', 'Motorbike'),
        ('car', 'Car'),
        ('three_wheeler', 'Three Wheeler'),
        ('bicycle', 'Bicycle'),
        ('lorry', 'Lorry'),
        ('truck', 'Truck'),
        ('van', 'Van'),
        ('bus', 'Bus'),
        ('coupe', 'Coupe'),
        ('suv', 'SUV (Sport Utility Vehicle)'),
        ('tractor', 'Tractor'),
        ('atv', 'ATV (All-Terrain Vehicle)'),
        ('sedan', 'Sedan'),
        ('limousine', 'Limousine'),
        ('electric_vehicle', 'Electric Vehicle'),
        ('hybrid_vehicle', 'Hybrid Vehicle'),
        ('offroad_vehicle', 'Off-Road Vehicle'),
        ('other', 'Other'),
    ]

    make = forms.ChoiceField(choices=MANUFACTURER_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    year_min = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Min year'}))
    year_max = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Max year'}))
    body_type = forms.ChoiceField(choices=BODYTYPE_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    color = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter color'}))

    price_min = forms.DecimalField(required=False, max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Min price'}))
    price_max = forms.DecimalField(required=False, max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Max price'}))

    mileage_min = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Min mileage'}))
    mileage_max = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Max mileage'}))

    engine_capacity_min = forms.DecimalField(required=False, max_digits=4, decimal_places=1, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Min engine capacity'}))
    engine_capacity_max = forms.DecimalField(required=False, max_digits=4, decimal_places=1, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Max engine capacity'}))

    transmission_type = forms.ChoiceField(choices=[('', 'Any'), ('Automatic', 'Automatic'), ('Manual', 'Manual')], required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    fuel_type = forms.ChoiceField(choices=[('', 'Any'), ('petrol', 'Petrol'), ('diesel', 'Diesel'), ('electric', 'Electric'), ('hybrid', 'Hybrid')], required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    engine_type = forms.ChoiceField(choices=[('', 'Any'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid'), ('Internal Combustion Engine', 'ICE (Internal Combustion Engine)')], required=False, widget=forms.Select(attrs={'class': 'form-control'}))

    abs_breaks = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    alloy_wheels = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    airbags = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    air_conditioning = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    power_steering = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    power_windows = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    central_locking = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    reverse_camera = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    sunroof = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    leather_seats = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

class VehicleComparisonForm(forms.Form):
    vehicle1 = forms.ModelChoiceField(queryset=Vehicle.objects.all(), label='Select Vehicle 1')
    vehicle2 = forms.ModelChoiceField(queryset=Vehicle.objects.all(), label='Select Vehicle 2')