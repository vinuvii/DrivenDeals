from django import forms

class BidForm(forms.Form):
    car_id = forms.IntegerField(widget=forms.HiddenInput())
    bid_amount = forms.DecimalField(max_digits=10, decimal_places=2)