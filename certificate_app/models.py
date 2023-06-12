from django.db import models

# Create your models here.

class Student_data(models.Model):
    name = models.CharField(max_length=200)
    student_id = models.CharField(max_length=200, blank=True, null=True)
    regis_number = models.CharField(max_length=29)
    course_name = models.CharField(max_length=400)
    father_name = models.CharField(max_length=200)
    date_of_birth = models.CharField(max_length=200)
    course_type = models.CharField(max_length=300)
    start_and_end_date = models.CharField(max_length=200)
    institute = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'Student_data'
        verbose_name_plural = 'Student_datas'

    def __str__(self):
     return str(self.name)
     
        
