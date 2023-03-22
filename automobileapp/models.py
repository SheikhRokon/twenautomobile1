from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
import string, random
from django.db import IntegrityError
from django.urls import reverse

 
# Create your models
class BannerSlider(models.Model):
    title_h5 = models.CharField(max_length = 200)
    title_h2 = models.CharField(max_length = 200) 
    title_p = models.CharField(max_length = 150) 
    image = models.ImageField(upload_to='BannerSlider')
    ordering  = models.IntegerField(unique=True,blank=True,null=True)

    def __str__(self):
        return self.title_h2


class CourseCategory(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 50, unique=True, blank=True, null=True)
    categorie_icon_code_To_icofont = models.CharField(max_length = 50)
    description =RichTextUploadingField()
    ordering  = models.IntegerField(unique=True,blank=True,null=True)
    
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            self.slug = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(49))
            super().save(*args, **kwargs)
        except IntegrityError:
            self.save(*args, **kwargs)

    class Meta:
        verbose_name = 'CourseCategory'
        verbose_name_plural = 'CourseCategories'

class TypeOfVehicles(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='VehiclesImage')
    parent =models.ForeignKey('self', on_delete=models.CASCADE,blank=True,null=True)
    slug = models.SlugField(max_length = 50, unique=True, blank=True, null=True)
    description =RichTextUploadingField(blank=True,null=True)
    ordering  = models.IntegerField(unique=True,blank=True,null=True)
    
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            self.slug = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(49))
            super().save(*args, **kwargs)
        except IntegrityError:
            self.save(*args, **kwargs)


    class Meta:
        verbose_name = 'TypeOfVehicles'
        verbose_name_plural = 'TypeOfVehicles'

class CourseType(models.Model):
    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length = 100)
    course_price =models.IntegerField()
    course_discount_price =models.IntegerField(blank=True, null=True)
    slug = models.SlugField(max_length = 50, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='CourseImage')
    course_duration_for_month = models.IntegerField(blank=True,null=True)
    course_duration_for_day = models.IntegerField(blank=True,null=True)
    course_duration_for_hours = models.IntegerField(blank=True,null=True)
    course_categorie  = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    type_of_vehicles = models.ForeignKey(TypeOfVehicles, on_delete=models.CASCADE)   
    description =RichTextUploadingField()
    ordering  = models.IntegerField(unique=True,blank=True,null=True)
    course_type = models.ForeignKey(CourseType, on_delete=models.CASCADE,blank=True,null=True)
    
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            self.slug = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(49))
            super().save(*args, **kwargs)
        except IntegrityError:
            self.save(*args, **kwargs)

    def get_add_to_cart_url(self):
        return reverse('add-to-cart', kwargs={
            'slug': self.slug
        })
    def get_remove_from_cart_url(self):
        return reverse('remove-form-cart', kwargs={
            'slug': self.slug
        })
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class UpcommingCourse(models.Model):
    title = models.CharField(max_length = 100)
    course_price =models.IntegerField()
    course_discount_price =models.IntegerField(blank=True, null=True)
    slug = models.SlugField(max_length = 50, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='UpcommingCourseImage')
    course_duration_for_month = models.IntegerField(blank=True,null=True)
    course_duration_for_day = models.IntegerField(blank=True,null=True)
    course_duration_for_hours = models.IntegerField(blank=True,null=True)
    course_categorie  = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    type_of_vehicles = models.ForeignKey(TypeOfVehicles, on_delete=models.CASCADE)   
    Course_Type =(
        ('Recored_Video_Course','Recored_Video_Course'),
        ('Online_Live_Course','Online_Live_Course'),
        ('Ofline_Live_Course','Ofline_Live_Course'),
    )
    course_type  = models.CharField(max_length = 150, choices=Course_Type)
    description =RichTextUploadingField()
    ordering  = models.IntegerField(unique=True,blank=True,null=True)
    
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        try:
            self.slug = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(49))
            super().save(*args, **kwargs)
        except IntegrityError:
            self.save(*args, **kwargs)

    class Meta:
        verbose_name = 'UpcommingCourse'
        verbose_name_plural = 'UpcommingCourse'

 
class ForEnquiry(models.Model):
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    place = models.CharField(max_length=200)
    course_type  = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    message  = models.TextField()
    

    def __str__(self):
        return self.f_name + ' '  + self.l_name   
    

class OurPartner(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='PartnerImage')
    ordering  = models.IntegerField(unique=True,blank=True,null=True)
    
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'OurPartner'
        verbose_name_plural = 'OurPartner'

class OurAlumnus(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='AlumnusImage')
    ordering  = models.IntegerField(unique=True,blank=True,null=True)
    
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'OurAlumnus'
        verbose_name_plural = 'OurAlumnus'

class Testimonial(models.Model):
    name = models.CharField(max_length = 100)
    designation = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='TestimonialImage')
    description =RichTextUploadingField()
    ordering  = models.IntegerField(unique=True,blank=True,null=True)
    
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Testimonial'

class OurInstructor(models.Model):
    name = models.CharField(max_length = 100)
    designation = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='OurInstructorImage')
    about_instructor =RichTextUploadingField(max_length = 1500)
    ordering  = models.IntegerField(unique=True,blank=True,null=True)
    facebook_http_link  = models.URLField(max_length = 200,blank=True,null=True)
    linkedin_http_link  = models.URLField(max_length = 200,blank=True,null=True)
    instagram_http_link  = models.URLField(max_length = 200,blank=True,null=True)
    
    
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'OurInstructor'

class FREQUENTLY_ASKED_QUESTIONS(models.Model):
    question = models.CharField(max_length = 50)
    answer =RichTextUploadingField(max_length = 200)
    ordering  = models.IntegerField(unique=True,blank=True,null=True)
    
    
    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'FREQUENTLY_ASKED_QUESTIONS'

class Certificate(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='Certificate')
    ordering  = models.IntegerField(unique=True,blank=True,null=True)


    def __str__(self):
        return self.title

class ImageGallery(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 50, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='ImageGallery')
    description =RichTextUploadingField()
    ordering  = models.IntegerField(unique=True,blank=True,null=True)

    def save(self, *args, **kwargs):
        try:
            self.slug = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(49))
            super().save(*args, **kwargs)
        except IntegrityError:
            self.save(*args, **kwargs)

    def __str__(self):
        return self.title

class VideoGallery(models.Model):
    title = models.CharField(max_length = 200)
    video_embed_link = models.URLField(max_length = 200)
    ordering  = models.IntegerField(unique=True,blank=True,null=True)


    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='Blog')
    description =RichTextUploadingField()
    post_date = models.DateField(default=timezone.now)
    ordering  = models.IntegerField(unique=True,blank=True,null=True)
    view_count = models.PositiveIntegerField(default=0)
    
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Blogs'

class BlogsComment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    blogs = models.ForeignKey('Blog', on_delete=models.CASCADE)


class NewsLetter(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email



class Notice(models.Model):
    title = models.CharField(max_length = 50)
    pdf_file = models.FileField(upload_to='Notice')
    date = models.DateTimeField(default=timezone.now)
    ordering  = models.IntegerField(unique=True,blank=True,null=True)
    
   
    def __str__(self):
        return self.title

    class Meta:
        ordering =['-id','ordering']



class DirectorMessage(models.Model):
    name = models.CharField(max_length = 50)
    designation = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='DirectorImage')
    message =RichTextUploadingField()
    ordering  = models.IntegerField(unique=True,blank=True,null=True)
   
    def __str__(self):
        return self.name

    class Meta:
        ordering =['ordering']

class Mission_and_Vission(models.Model):
    mission =RichTextUploadingField()
    vission =RichTextUploadingField()

class Event(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 50, unique=True)
    image = models.ImageField(upload_to='EventImage')
    mesdescription = RichTextUploadingField()
    date = models.DateTimeField(default=timezone.now)
    ordering  = models.IntegerField(unique=True,blank=True,null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            self.slug = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(49))
            super().save(*args, **kwargs)
        except IntegrityError:
            self.save(*args, **kwargs)

    class Meta:
        ordering =['ordering']

class MediaCovarage(models.Model):
    title = models.CharField(max_length = 100)
    video_embed_link = models.URLField(max_length = 500,blank=True,null=True)
    description = RichTextUploadingField()
    date = models.DateTimeField(default=timezone.now)
    ordering  = models.IntegerField(unique=True,blank=True,null=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering =['ordering']
        
class Countdown(models.Model):
    GRADUTED_FROM_HERE = models.IntegerField()
    NUMBER_OF_INSTRUCTOR = models.IntegerField()
    YEARS_ON_MARKET = models.IntegerField()
    PRESENT_STUDENTS = models.IntegerField()
    
    def __str__(self):
        return str(self.GRADUTED_FROM_HERE)

