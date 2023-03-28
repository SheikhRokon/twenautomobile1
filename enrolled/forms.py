from django import forms
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

class bookingstudentFrom(forms.ModelForm):
    name = forms.CharField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : "Your Name" }))

    email = forms.EmailField(widget= forms.EmailInput(attrs ={
        'class': 'form-control', 
        'placeholder':"Your Email" }))

    phone = forms.CharField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : "Your Number" }))

    course = forms.CharField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : "Your Course" }))    
    
    permanent_a = forms.CharField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : "Your Permanent Address" }))

    present_a = forms.CharField(widget= forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : "Your Present Address" }))

    class Meta:
        model = BokingNow
        fields = '__all__'
