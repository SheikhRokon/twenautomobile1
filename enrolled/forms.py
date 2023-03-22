from django import forms
from .models import Order
from .models import *
 
class OrderPaymentForm(forms.Form):
    PAYMENT_Method =(
    # ('Bkash', 'Bkash'),
    ('Nagad', 'Nagad'),
    ('Roket', 'Roket'),
)
    payment_method = forms.ChoiceField(choices=PAYMENT_Method,widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    your_payment_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    pyamnet_transaction_id = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    class Meta:
        model = OrderPayment
        fields = ['payment_method','your_payment_number','pyamnet_transaction_id']

PAYMENT_CHOICES =(
    # ('Bkash', 'Bkash'),
    ('Nagad', 'Nagad'),
    ('Roket', 'Roket'),
)

class PaymentMethodForm(forms.ModelForm):
    payment_option = forms.ChoiceField(widget=forms.RadioSelect(attrs={
        'class':' collapsed'       
    }), choices=PAYMENT_CHOICES)

    class Meta:
        model = Order
        fields = ['payment_option']
