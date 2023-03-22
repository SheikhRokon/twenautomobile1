from django import forms
from .models import *
from django.forms import ModelChoiceField

class BlogCommentForm(forms.Form):
    author = forms.CharField(max_length=50,
    
    widget=forms.TextInput( attrs={
        "class": "form-control border-0",
        "placeholder": "Your Name"

    })
    )
    body = forms.CharField(
        widget=forms.Textarea(attrs={
            "class":"form-control border-0",
            "placeholder":"Leave a comment",
            'rows':"3"
        })
        )


class NewsLetterForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder':"Enter email"
        }))
    class Meta:
        model = NewsLetter
        fields = ['email']


class ForEnquiryForm(forms.ModelForm):
    full_name  = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder':"Full Name"
        }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder':"Email"
        }))
    phone  = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder':"Contact Number"
        }))  

    place  = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder':"Place"
        })) 
     
    course_type  = ModelChoiceField(queryset=Course.objects.all(),empty_label="Select Course",widget=forms.Select(attrs={
        'placeholder':"Enter Course",
        'class':'form-control  fec'
        }))

    message  = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder':"message",
        'rows':"3"
        })) 
    class Meta:
        model = ForEnquiry
        fields ='__all__'


