
from django import forms

class PaymentForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    payment_method = forms.ChoiceField(choices=[
        ('mtn', 'MTN Mobile Money'),
        ('orange', 'Orange Money'),
    ])
    phone_number = forms.CharField(max_length=15, required=False)