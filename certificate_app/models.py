from django.db import models

# Create your models here.

class Student_data(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    number = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Student_data'
        verbose_name_plural = 'Student_datas'

    def __str__(self):
     return str(self.name)
        
