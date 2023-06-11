from import_export import resources
from .models import *


class Student_Resource(resources.ModelResource):

    class Meta:
        model = Student_data