
from django import forms
from .models import Student_data

class PersonData(forms.Form):
	class meta:
		model = Student_data
		fields = '__all__'