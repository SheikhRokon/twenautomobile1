from django.urls import path
from .views import *

urlpatterns = [
    path('student_data/',student_data, name='student_data' ),

]