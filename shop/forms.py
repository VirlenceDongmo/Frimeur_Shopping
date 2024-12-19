
from django import forms

class PaymentForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    payment_method = forms.ChoiceField(choices=[
        ('mtn', 'MTN Mobile Money'),
        ('orange', 'Orange Money'),
        ('card', 'Carte Bancaire'),
    ])
    phone_number = forms.CharField(max_length=15, required=False)
    card_number = forms.CharField(max_length=16, required=False)
    expiry_date = forms.CharField(max_length=5, required=False)
    cvv = forms.CharField(max_length=3, required=False)