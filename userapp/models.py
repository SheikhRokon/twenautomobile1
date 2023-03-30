from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
import string, random
from django.db import IntegrityError
from django.utils import timezone

class User(AbstractUser):
    phone = models.CharField(max_length = 15)
    is_admin= models.BooleanField('Is admin', default=False)
    is_student = models.BooleanField('Is customer', default=False)
    is_instructor = models.BooleanField('Is instructor', default=False)
    is_employee = models.BooleanField('Is employee', default=False)
    
    


class Profile(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE, max_length=1)
    image               = models.ImageField(upload_to="profilepicture", default='no_img.png')
    date_of_birthday    = models.DateField(auto_now_add=False,blank=True,null=True)
    permanent_address   = models.CharField(max_length=100,blank=True,null=True)
    present_address     = models.CharField(max_length=100,blank=True,null=True)
    profile_registration = models.DateField(default=timezone.now,blank=True,null=True)
    

    def __str__(self):
        return self.user.username


class ConductData(models.Model):
    name = models.CharField(max_length = 150)
    email = models.EmailField()
    phone = models.CharField(max_length = 15)
    subject  = models.CharField(max_length = 150)
    message  = models.TextField()
    
    def __str__(self):
        return self.name + ' /' + self.email

    class Meta:
        verbose_name = 'ConductData'
        verbose_name_plural = 'ConductData'

class Career(models.Model):
    title = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='CareerImage',default='noimg.jpg')
    slug = models.SlugField(max_length = 50)
    active_status = models.BooleanField(default=True)
    job_description =RichTextField()
    job_requirement =RichTextField()
    educational_eequirements =RichTextField()
    compensation_other_benefits =RichTextField()
    experience = models.CharField(max_length = 150) 
    salary = models.CharField(max_length = 150)
    date = models.DateField(auto_now=False, auto_now_add=False)
    end_date  = models.DateTimeField(default=timezone.now,auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title 

    def save(self, *args, **kwargs):
        try:
            self.slug = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(49))
            super().save(*args, **kwargs)
        except IntegrityError:
            self.save(*args, **kwargs)

class JobApplication(models.Model):
    full_name= models.CharField(max_length = 150)
    email = models.EmailField()
    phone= models.CharField(max_length = 150)
    expected_salary= models.CharField(max_length = 150)
    cv= models.FileField(upload_to='ApplicationCV')
    message = models.TextField()
    
    def __str__(self):
        return self.email


class UserIp(models.Model):
    id = models.BigAutoField(primary_key = True, unique=True)
    user_ip = models.CharField(max_length = 150,unique=False)
    country = models.CharField(max_length=1500, blank=True, null=True)
    division = models.CharField(max_length=1500, blank=True, null=True)
    city = models.CharField(max_length=1500, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.user_ip
    

