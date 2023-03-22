from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

class UpdateRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields =[ 'username', 'first_name', 'last_name', 'email','phone']

class UpdateProfileForm(forms.ModelForm):
    date_of_birthday = forms.DateField(
        widget=forms.TextInput( attrs={
        "type":"date",
    })
    )
    class Meta:
        model = Profile
        fields = ['image','date_of_birthday','permanent_address','present_address']

class Contact_Form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Name',
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Your Email',
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Phone',
    }))

    subject = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Subject',
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder':'Your Message',

    }))
    
    class Meta:
        model = ConductData
        fields = '__all__'

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields ='__all__'


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,
               widget=forms.TextInput(attrs={
                   "class":"form-control",
                   "placeholder":"Enter your first name.."
               }) 
               )
    last_name = forms.CharField(max_length=30,
            widget=forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Enter your second name.."
            }) 
            )
    username = forms.CharField(max_length=30,label = "Username Or Email",
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Enter your username or email"
        }) 
        )
    email = forms.EmailField(label = "Verification Email",
            widget=forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Enter your verify email.."
            }) 
            )
    phone =  email = forms.CharField(
            widget=forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Enter your phone number"
            }) 
            )
    class Meta:
        model=User
        fields =['username','first_name', 'last_name',  'email','phone']
        
 
        
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(label = "Username Or Email",widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your username or email',}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        }
))
        