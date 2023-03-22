from userapp.models import *
from automobileapp.models import *
from enrolled.models import *
from django import forms
from ckeditor.widgets import CKEditorWidget

class UserIpForm(forms.ModelForm):
    class Meta:
        model = UserIp 
        fields = '__all__'

class CareerForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'type':'date'
    }))
    end_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        'type':'datetime-local'
    }))
    class Meta:
        model = Career 
        fields = '__all__'

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication 
        fields = '__all__'

class ForEnquiryForm(forms.ModelForm):
    class Meta:
        model = ForEnquiry
        fields = '__all__' 

class BannerSliderForm(forms.ModelForm):
    class Meta:
        model = BannerSlider
        fields = '__all__' 

class CourseCategoryForm(forms.ModelForm):
    class Meta:
        model = CourseCategory
        fields = '__all__' 


class TypeOfVehiclesForm(forms.ModelForm):
    class Meta:
        model = TypeOfVehicles
        fields = '__all__'

class CourseTypeForm(forms.ModelForm):
    class Meta:
        model = CourseType
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class UpcommingCourseForm(forms.ModelForm):
    class Meta:
        model = UpcommingCourse
        fields = '__all__' 


class OurAlumnusForm(forms.ModelForm):
    class Meta:
        model = OurAlumnus 
        fields = '__all__' 
    

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial 
        fields = '__all__'

class OurInstructorForm(forms.ModelForm):
    class Meta:
        model = OurInstructor 
        fields = '__all__'

class FqaForm(forms.ModelForm):
    class Meta:
        model = FREQUENTLY_ASKED_QUESTIONS
        fields = '__all__'

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'

class ImageGalleryForm(forms.ModelForm):
    class Meta:
        model = ImageGallery
        fields = '__all__'

class VideoGalleryForm(forms.ModelForm):
    class Meta:
        model = VideoGallery
        fields = '__all__'  

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'  

class BlogsCommentForm(forms.ModelForm):
    class Meta:
        model = BlogsComment
        fields = '__all__' 

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = '__all__'

class DirectorMessageForm(forms.ModelForm):
    class Meta:
        model = DirectorMessage
        fields = '__all__'

class Mission_and_VissionForm(forms.ModelForm):
    class Meta:
        model = Mission_and_Vission
        fields = '__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class MediaCovarageForm(forms.ModelForm):
    class Meta:
        model = MediaCovarage
        fields = '__all__'


class CountdownForm(forms.ModelForm):
    class Meta:
        model = Countdown
        fields = '__all__'