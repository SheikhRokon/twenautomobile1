from .forms import *
from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
# inport_export
from import_export import resources 
from tablib import Dataset
from .resources import Student_Resource


# Create your views here.

def student_data(request):
    if request.method == 'POST':
        student_resource= Student_Resource()
        dataset = Dataset()
        new_studebt = request.FILES['myfile']

        if not new_studebt.name.endswith('xlsx'):
            messages.info(request,'!Wrong Format')
            return render(request,'inputform.html')

        import_data = dataset.load(new_studebt.read(),format='xlsx')
        for data in import_data:
            value = Student_data(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                )
            value.save()
            return redirect('student_cer_data-list')
    return render(request, 'inputform.html')
