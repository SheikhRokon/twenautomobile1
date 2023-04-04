from django.shortcuts import render, redirect
from userapp.models import *
from automobileapp.models import *
from enrolled.models import *
from .forms import *

# Create your views here.
from django.contrib import messages

from django.utils import timezone
from datetime import timedelta, datetime,date
now = timezone.now()
# Create your views here.

def dashboard_home(request):
    total_visit_unique = UserIp.objects.all().values_list('user_ip', flat=True).distinct().count()
    total_visit = UserIp.objects.all().count()
    today_total_visit = UserIp.objects.filter(date__gte=date.today()).count()
    today_total_visit_unique = UserIp.objects.filter(date__gte=date.today()).values_list('user_ip', flat=True).distinct().count()



    context ={
        'total_visit':total_visit,
        'total_visit_unique':total_visit_unique,
        'today_total_visit':today_total_visit,
        'today_total_visit_unique':today_total_visit_unique,
    }
    return render(request, 'dashboard/index.html', context)


#visitor

def visitor_list(request):
    visitor_list = UserIp.objects.all().order_by('-id')
    return render(request, 'dashboard/visitor/list.html', {'visitor_list':visitor_list})

def today_visitor_list(request):
    visitor_list = UserIp.objects.filter(date__gte=date.today()).order_by('-id')
    return render(request, 'dashboard/visitor/today-list.html', {'visitor_list':visitor_list})

def unique_visitor_list(request):
    visitor_list = UserIp.objects.all().values_list('user_ip','country','division','city').distinct()
    return render(request, 'dashboard/visitor/unique-list.html', {'visitor_list':visitor_list})


def today_unique_visitor_list(request):
    visitor_list =  UserIp.objects.filter(date__gte=date.today()).values_list('user_ip','country','division','city').distinct()
    return render(request, 'dashboard/visitor/todayunique-list.html', {'visitor_list':visitor_list})



def visitor_edit(request,pk):
    visitor = UserIp.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserIpForm(request.POST,request.FILES,instance=visitor)
        if form.is_valid():
            form.save()
            return redirect('visitor-list')
    else:
        form = UserIpForm(instance=visitor)
    return render(request, 'dashboard/visitor/add.html', {'form':form})


def visitor_delete(request,pk):
    visitor=UserIp.objects.get(pk=pk)
    visitor.delete()
    messages.success(request, 'Successfully delete')
    return redirect('visitor-list')

# career

def career_list(request):
    career_list = Career.objects.all().order_by('-id')
    return render(request, 'dashboard/career/list.html', {'career_list':career_list})



def career_add(request):
    if request.method == 'POST':
        form = CareerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('career-list')
    else:
        form = CareerForm()
    return render(request, 'dashboard/career/add.html', {'form':form})



def career_edit(request,pk):
    career = Career.objects.get(pk=pk)
    if request.method == 'POST':
        form = CareerForm(request.POST,request.FILES,instance=career)
        if form.is_valid():
            form.save()
            return redirect('career-list')
        else:
            return redirect('career-add')
    else:
        form = CareerForm(instance=career)
    return render(request, 'dashboard/career/add.html', {'form':form})


def career_delete(request,pk):
    career=Career.objects.get(pk=pk)
    career.delete()
    messages.success(request, 'Successfully delete')
    return redirect('career-list')


# jobapplication

def jobapplication_list(request):
    jobapplication_list = JobApplication.objects.all().order_by('-id')
    return render(request, 'dashboard/jobapplication/list.html', {'jobapplication_list':jobapplication_list})



def jobapplication_add(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('jobapplication-list')
    else:
        form = JobApplicationForm()
    return render(request, 'dashboard/jobapplication/add.html', {'form':form})



def jobapplication_edit(request,pk):
    jobapplication = JobApplication.objects.get(pk=pk)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST,request.FILES,instance=jobapplication)
        if form.is_valid():
            form.save()
            return redirect('jobapplication-list')
        else:
            return redirect('jobapplication-add')
    else:
        form = JobApplicationForm(instance=jobapplication)
    return render(request, 'dashboard/jobapplication/add.html', {'form':form})


def jobapplication_delete(request,pk):
    jobapplication=Jobapplication.objects.get(pk=pk)
    jobapplication.delete()
    messages.success(request, 'Successfully delete')
    return redirect('jobapplication-list')


# forenquiry

def forenquiry_list(request):
    forenquiry_list = ForEnquiry.objects.all().order_by('-id')
    return render(request, 'dashboard/forenquiry/list.html', {'forenquiry_list':forenquiry_list})

def forenquiry_add(request):
    if request.method == 'POST':
        form = ForEnquiryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('forenquiry-list')
    else:
        form = ForEnquiryForm()
    return render(request, 'dashboard/forenquiry/add.html', {'form':form})

def forenquiry_edit(request,pk):
    forenquiry = ForEnquiry.objects.get(pk=pk)
    if request.method == 'POST':
        form = ForEnquiryForm(request.POST,request.FILES,instance=forenquiry)
        if form.is_valid():
            form.save()
            return redirect('forenquiry-list') 
        else:
            return redirect('forenquiry-add')
    else:
        form = ForEnquiryForm(instance=forenquiry)
    return render(request, 'dashboard/forenquiry/add.html', {'form':form})


def forenquiry_delete(request,pk):
    forenquiry=ForEnquiry.objects.get(pk=pk)
    forenquiry.delete()
    messages.success(request, 'Successfully delete')
    return redirect('forenquiry-list')

# banner

def banner_list(request):
    banner_list = BannerSlider.objects.all().order_by('-id')
    return render(request, 'dashboard/banner/list.html', {'banner_list':banner_list})

def banner_add(request):
    if request.method == 'POST':
        form = BannerSliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('banner-list')
    else:
        form = BannerSliderForm()
    return render(request, 'dashboard/banner/add.html', {'form':form})

def banner_edit(request,pk):
    banner = BannerSlider.objects.get(pk=pk)
    if request.method == 'POST':
        form = BannerSlideForm(request.POST,request.FILES,instance=banner)
        if form.is_valid():
            form.save()
            return redirect('banner-list') 
        else:
            return redirect('banner-add')
    else:
        form = BannerSlideForm(instance=banner)
    return render(request, 'dashboard/banner/add.html', {'form':form})


def banner_delete(request,pk):
    banner=BannerSlider.objects.get(pk=pk)
    banner.delete()
    messages.success(request, 'Successfully delete')
    return redirect('banner-list')

# coursecategory

def coursecategory_list(request):
    coursecategory_list = CourseCategory.objects.all().order_by('-id')
    return render(request, 'dashboard/coursecategory/list.html', {'coursecategory_list':coursecategory_list})

def coursecategory_add(request):
    if request.method == 'POST':
        form = CourseCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('coursecategory-list')
    else:
        form = CourseCategoryForm()
    return render(request, 'dashboard/coursecategory/add.html', {'form':form})

def coursecategory_edit(request,pk):
    coursecategory = CourseCategory.objects.get(pk=pk)
    if request.method == 'POST':
        form = CourseCategoryForm(request.POST,request.FILES,instance=coursecategory)
        if form.is_valid():
            form.save()
            return redirect('coursecategory-list') 
        else:
            return redirect('coursecategory-add')
    else:
        form = CourseCategoryForm(instance=coursecategory)
    return render(request, 'dashboard/coursecategory/add.html', {'form':form})


def coursecategory_delete(request,pk):
    coursecategory=CourseCategory.objects.get(pk=pk)
    coursecategory.delete()
    messages.success(request, 'Successfully delete')
    return redirect('coursecategory-list')

# typeofvehicles

def typeofvehicles_list(request):
    typeofvehicles_list = TypeOfVehicles.objects.all().order_by('-id')
    return render(request, 'dashboard/typeofvehicles/list.html', {'typeofvehicles_list':typeofvehicles_list})

def typeofvehicles_add(request):
    if request.method == 'POST':
        form = TypeOfVehiclesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('typeofvehicles-list')
    else:
        form = TypeOfVehiclesForm()
    return render(request, 'dashboard/typeofvehicles/add.html', {'form':form})

def typeofvehicles_edit(request,pk):
    typeofvehicles = TypeOfVehicles.objects.get(pk=pk)
    if request.method == 'POST':
        form = TypeOfVehiclesForm(request.POST,request.FILES,instance=typeofvehicles)
        if form.is_valid():
            form.save()
            return redirect('typeofvehicles-list') 
        else:
            return redirect('typeofvehicles-add')
    else:
        form = TypeOfVehiclesForm(instance=typeofvehicles)
    return render(request, 'dashboard/typeofvehicles/add.html', {'form':form})


def typeofvehicles_delete(request,pk):
    typeofvehicles=TypeOfVehicles.objects.get(pk=pk)
    typeofvehicles.delete()
    messages.success(request, 'Successfully delete')
    return redirect('typeofvehicles-list')

# coursetype

def coursetype_list(request):
    coursetype_list = CourseType.objects.all().order_by('-id')
    return render(request, 'dashboard/coursetype/list.html', {'coursetype_list':coursetype_list})

def coursetype_add(request):
    if request.method == 'POST':
        form = CourseTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('coursetype-list')
    else:
        form = CourseTypeForm()
    return render(request, 'dashboard/coursetype/add.html', {'form':form})

def coursetype_edit(request,pk):
    coursetype = CourseType.objects.get(pk=pk)
    if request.method == 'POST':
        form = CourseTypeForm(request.POST,request.FILES,instance=coursetype)
        if form.is_valid():
            form.save()
            return redirect('coursetype-list') 
        else:
            return redirect('coursetype-add')
    else:
        form = CourseTypeForm(instance=coursetype)
    return render(request, 'dashboard/coursetype/add.html', {'form':form})


def coursetype_delete(request,pk):
    coursetype=CourseType.objects.get(pk=pk)
    coursetype.delete()
    messages.success(request, 'Successfully delete')
    return redirect('coursetype-list')

# course

def course_list(request):
    course_list = Course.objects.all().order_by('-id')
    return render(request, 'dashboard/course/list.html', {'course_list':course_list})

def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course-list')
    else:
        form = CourseForm()
    return render(request, 'dashboard/course/add.html', {'form':form})

def course_edit(request,pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST,request.FILES,instance=course)
        if form.is_valid():
            form.save()
            return redirect('course-list') 
        else:
            return redirect('course-add')
    else:
        form = CourseForm(instance=course)
    return render(request, 'dashboard/course/add.html', {'form':form})


def course_delete(request,pk):
    course=Course.objects.get(pk=pk)
    course.delete()
    messages.success(request, 'Successfully delete')
    return redirect('course-list')


# upcomingcourse

def upcomingcourse_list(request):
    upcomingcourse_list = UpcommingCourse.objects.all().order_by('-id')
    return render(request, 'dashboard/upcomingcourse/list.html', {'upcomingcourse_list':upcomingcourse_list})

def upcomingcourse_add(request):
    if request.method == 'POST':
        form = UpcommingCourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upcomingcourse-list')
    else:
        form = UpcommingCourseForm()
    return render(request, 'dashboard/upcomingcourse/add.html', {'form':form})

def upcomingcourse_edit(request,pk):
    upcomingcourse = UpcommingCourse.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpcommingCourseForm(request.POST,request.FILES,instance=upcomingcourse)
        if form.is_valid():
            form.save()
            return redirect('upcomingcourse-list') 
        else:
            return redirect('upcomingcourse-add')
    else:
        form = UpcommingCourseForm(instance=upcomingcourse)
    return render(request, 'dashboard/upcomingcourse/add.html', {'form':form})


def upcomingcourse_delete(request,pk):
    upcomingcourse=UpcommingCourse.objects.get(pk=pk)
    upcomingcourse.delete()
    messages.success(request, 'Successfully delete')
    return redirect('upcomingcourse-list')


# alumnus

def alumnus_list(request):
    alumnus_list = OurAlumnus.objects.all().order_by('-id')
    return render(request, 'dashboard/alumnus/list.html', {'alumnus_list':alumnus_list})

def alumnus_add(request):
    if request.method == 'POST':
        form = OurAlumnusForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('alumnus-list')
    else:
        form = alumnusForm()
    return render(request, 'dashboard/alumnus/add.html', {'form':form})

def alumnus_edit(request,pk):
    alumnus = OurAlumnus.objects.get(pk=pk)
    if request.method == 'POST':
        form = OurAlumnusForm(request.POST,request.FILES,instance=alumnus)
        if form.is_valid():
            form.save()
            return redirect('alumnus-list') 
        else:
            return redirect('alumnus-add')
    else:
        form = OurAlumnusForm(instance=alumnus)
    return render(request, 'dashboard/alumnus/add.html', {'form':form})


def alumnus_delete(request,pk):
    alumnus=alumnus.objects.get(pk=pk)
    alumnus.delete()
    messages.success(request, 'Successfully delete')
    return redirect('alumnus-list')


# testimonial

def testimonial_list(request):
    testimonial_list = Testimonial.objects.all().order_by('-id')
    return render(request, 'dashboard/testimonial/list.html', {'testimonial_list':testimonial_list})

def testimonial_add(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('testimonial-list')
    else:
        form = TestimonialForm()
    return render(request, 'dashboard/testimonial/add.html', {'form':form})

def testimonial_edit(request,pk):
    testimonial = Testimonial.objects.get(pk=pk)
    if request.method == 'POST':
        form = TestimonialForm(request.POST,request.FILES,instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('testimonial-list') 
        else:
            return redirect('testimonial-add')
    else:
        form = TestimonialForm(instance=testimonial)
    return render(request, 'dashboard/testimonial/add.html', {'form':form})


def testimonial_delete(request,pk):
    testimonial=Testimonial.objects.get(pk=pk)
    testimonial.delete()
    messages.success(request, 'Successfully delete')
    return redirect('testimonial-list')

# instructor

def instructor_list(request):
    instructor_list = OurInstructor.objects.all().order_by('-id')
    return render(request, 'dashboard/instructor/list.html', {'instructor_list':instructor_list})

def instructor_add(request):
    if request.method == 'POST':
        form = OurInstructorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('instructor-list')
    else:
        form = OurInstructorForm()
    return render(request, 'dashboard/instructor/add.html', {'form':form})

def instructor_edit(request,pk):
    instructor = OurInstructor.objects.get(pk=pk)
    if request.method == 'POST':
        form = OurInstructorForm(request.POST,request.FILES,instance=instructor)
        if form.is_valid():
            form.save()
            return redirect('instructor-list') 
        else:
            return redirect('instructor-add')
    else:
        form = OurInstructorForm(instance=instructor)
    return render(request, 'dashboard/instructor/add.html', {'form':form})


def instructor_delete(request,pk):
    instructor=OurInstructor.objects.get(pk=pk)
    instructor.delete()
    messages.success(request, 'Successfully delete')
    return redirect('instructor-list')


# fqa

def fqa_list(request):
    fqa_list = FREQUENTLY_ASKED_QUESTIONS.objects.all().order_by('-id')
    return render(request, 'dashboard/fqa/list.html', {'fqa_list':fqa_list})

def fqa_add(request):
    if request.method == 'POST':
        form = FqaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fqa-list')
    else:
        form = FqaForm()
    return render(request, 'dashboard/fqa/add.html', {'form':form})

def fqa_edit(request,pk):
    fqa = FREQUENTLY_ASKED_QUESTIONS.objects.get(pk=pk)
    if request.method == 'POST':
        form = FqaForm(request.POST,request.FILES,instance=fqa)
        if form.is_valid():
            form.save()
            return redirect('fqa-list') 
        else:
            return redirect('fqa-add')
    else:
        form = FqaForm(instance=fqa)
    return render(request, 'dashboard/fqa/add.html', {'form':form})


def fqa_delete(request,pk):
    fqa=FREQUENTLY_ASKED_QUESTIONS.objects.get(pk=pk)
    fqa.delete()
    messages.success(request, 'Successfully delete')
    return redirect('fqa-list')

# certificate

def certificate_list(request):
    certificate_list = Certificate.objects.all().order_by('-id')
    return render(request, 'dashboard/certificate/list.html', {'certificate_list':certificate_list})

def certificate_add(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('certificate-list')
    else:
        form = CertificateForm()
    return render(request, 'dashboard/certificate/add.html', {'form':form})

def certificate_edit(request,pk):
    certificate = Certificate.objects.get(pk=pk)
    if request.method == 'POST':
        form = CertificateForm(request.POST,request.FILES,instance=certificate)
        if form.is_valid():
            form.save()
            return redirect('certificate-list') 
        else:
            return redirect('certificate-add')
    else:
        form = CertificateForm(instance=certificate)
    return render(request, 'dashboard/certificate/add.html', {'form':form})


def certificate_delete(request,pk):
    certificate=Certificate.objects.get(pk=pk)
    certificate.delete()
    messages.success(request, 'Successfully delete')
    return redirect('certificate-list')

# imagegallery

def imagegallery_list(request):
    imagegallery_list = ImageGallery.objects.all().order_by('-id')
    return render(request, 'dashboard/imagegallery/list.html', {'imagegallery_list':imagegallery_list})

def imagegallery_add(request):
    if request.method == 'POST':
        form = ImageGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('imagegallery-list')
    else:
        form = ImageGalleryForm()
    return render(request, 'dashboard/imagegallery/add.html', {'form':form})

def imagegallery_edit(request,pk):
    imagegallery = ImageGallery.objects.get(pk=pk)
    if request.method == 'POST':
        form = ImageGalleryForm(request.POST,request.FILES,instance=imagegallery)
        if form.is_valid():
            form.save()
            return redirect('imagegallery-list') 
        else:
            return redirect('imagegallery-add')
    else:
        form = ImageGalleryForm(instance=imagegallery)
    return render(request, 'dashboard/imagegallery/add.html', {'form':form})


def imagegallery_delete(request,pk):
    imagegallery=ImageGallery.objects.get(pk=pk)
    imagegallery.delete()
    messages.success(request, 'Successfully delete')
    return redirect('imagegallery-list')

# videogallery

def videogallery_list(request):
    videogallery_list = VideoGallery.objects.all().order_by('-id')
    return render(request, 'dashboard/videogallery/list.html', {'videogallery_list':videogallery_list})

def videogallery_add(request):
    if request.method == 'POST':
        form = VideoGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('videogallery-list')
    else:
        form = VideoGalleryForm()
    return render(request, 'dashboard/videogallery/add.html', {'form':form})

def videogallery_edit(request,pk):
    videogallery = VideoGallery.objects.get(pk=pk)
    if request.method == 'POST':
        form = VideoGalleryForm(request.POST,request.FILES,instance=videogallery)
        if form.is_valid():
            form.save()
            return redirect('videogallery-list') 
        else:
            return redirect('videogallery-add')
    else:
        form = VideoGalleryForm(instance=videogallery)
    return render(request, 'dashboard/videogallery/add.html', {'form':form})


def videogallery_delete(request,pk):
    videogallery=VideoGallery.objects.get(pk=pk)
    videogallery.delete()
    messages.success(request, 'Successfully delete')
    return redirect('videogallery-list')


# blog

def blog_list(request):
    blog_list = Blog.objects.all().order_by('-id')
    return render(request, 'dashboard/blog/list.html', {'blog_list':blog_list})

def blog_add(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog-list')
    else:
        form = BlogForm()
    return render(request, 'dashboard/blog/add.html', {'form':form})

def blog_edit(request,pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog-list') 
        else:
            return redirect('blog-add')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'dashboard/blog/add.html', {'form':form})


def blog_delete(request,pk):
    blog=Blog.objects.get(pk=pk)
    blog.delete()
    messages.success(request, 'Successfully delete')
    return redirect('blog-list')

# blogcomments

def blogcomments_list(request):
    blogcomments_list = BlogsComment.objects.all().order_by('-id')
    return render(request, 'dashboard/blogcomments/list.html', {'blogcomments_list':blogcomments_list})

def blogcomments_add(request):
    if request.method == 'POST':
        form = BlogsCommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogcomments-list')
    else:
        form = BlogsCommentForm()
    return render(request, 'dashboard/blogcomments/add.html', {'form':form})

def blogcomments_edit(request,pk):
    blogcomments = BlogsComment.objects.get(pk=pk)
    if request.method == 'POST':
        form = BlogsCommentForm(request.POST,request.FILES,instance=blogcomments)
        if form.is_valid():
            form.save()
            return redirect('blogcomments-list') 
        else:
            return redirect('blogcomments-add')
    else:
        form = BlogsCommentForm(instance=blogcomments)
    return render(request, 'dashboard/blogcomments/add.html', {'form':form})


def blogcomments_delete(request,pk):
    blogcomments=BlogsComment.objects.get(pk=pk)
    blogcomments.delete()
    messages.success(request, 'Successfully delete')
    return redirect('blogcomments-list')

# newsletter

def newsletter_list(request):
    newsletter_list = NewsLetter.objects.all().order_by('-id')
    return render(request, 'dashboard/newsletter/list.html', {'newsletter_list':newsletter_list})

def newsletter_add(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('newsletter-list')
    else:
        form = NewsLetterForm()
    return render(request, 'dashboard/newsletter/add.html', {'form':form})

def newsletter_edit(request,pk):
    newsletter = NewsLetter.objects.get(pk=pk)
    if request.method == 'POST':
        form = NewsLetterForm(request.POST,request.FILES,instance=newsletter)
        if form.is_valid():
            form.save()
            return redirect('newsletter-list') 
        else:
            return redirect('newsletter-add')
    else:
        form = NewsLetterForm(instance=newsletter)
    return render(request, 'dashboard/newsletter/add.html', {'form':form})


def newsletter_delete(request,pk):
    newsletter=NewsLetter.objects.get(pk=pk)
    newsletter.delete()
    messages.success(request, 'Successfully delete')
    return redirect('newsletter-list')

# notice

def notice_list(request):
    notice_list = Notice.objects.all().order_by('-id')
    return render(request, 'dashboard/notice/list.html', {'notice_list':notice_list})

def notice_add(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('notice-list')
    else:
        form = NoticeForm()
    return render(request, 'dashboard/notice/add.html', {'form':form})

def notice_edit(request,pk):
    notice = Notice.objects.get(pk=pk)
    if request.method == 'POST':
        form = NoticeForm(request.POST,request.FILES,instance=notice)
        if form.is_valid():
            form.save()
            return redirect('notice-list') 
        else:
            return redirect('notice-add')
    else:
        form = NoticeForm(instance=notice)
    return render(request, 'dashboard/notice/add.html', {'form':form})


def notice_delete(request,pk):
    notice=Notice.objects.get(pk=pk)
    notice.delete()
    messages.success(request, 'Successfully delete')
    return redirect('notice-list')

# directormessage

def directormessage_list(request):
    directormessage_list = DirectorMessage.objects.all().order_by('-id')
    return render(request, 'dashboard/directormessage/list.html', {'directormessage_list':directormessage_list})

def directormessage_add(request):
    if request.method == 'POST':
        form = DirectorMessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('directormessage-list')
    else:
        form = DirectorMessageForm()
    return render(request, 'dashboard/directormessage/add.html', {'form':form})

def directormessage_edit(request,pk):
    directormessage = DirectorMessage.objects.get(pk=pk)
    if request.method == 'POST':
        form = DirectorMessageForm(request.POST,request.FILES,instance=directormessage)
        if form.is_valid():
            form.save()
            return redirect('directormessage-list') 
        else:
            return redirect('directormessage-add')
    else:
        form = DirectorMessageForm(instance=directormessage)
    return render(request, 'dashboard/directormessage/add.html', {'form':form})


def directormessage_delete(request,pk):
    directormessage=DirectorMessage.objects.get(pk=pk)
    directormessage.delete()
    messages.success(request, 'Successfully delete')
    return redirect('directormessage-list')


# missionvission

def missionvission_list(request):
    missionvission_list = Mission_and_Vission.objects.all().order_by('-id')
    return render(request, 'dashboard/missionvission/list.html', {'missionvission_list':missionvission_list})

def missionvission_add(request):
    if request.method == 'POST':
        form = Mission_and_VissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('missionvission-list')
    else:
        form = Mission_and_VissionForm()
    return render(request, 'dashboard/missionvission/add.html', {'form':form})

def missionvission_edit(request,pk):
    missionvission = Mission_and_Vission.objects.get(pk=pk)
    if request.method == 'POST':
        form = Mission_and_VissionForm(request.POST,request.FILES,instance=missionvission)
        if form.is_valid():
            form.save()
            return redirect('missionvission-list') 
        else:
            return redirect('missionvission-add')
    else:
        form = Mission_and_VissionForm(instance=missionvission)
    return render(request, 'dashboard/missionvission/add.html', {'form':form})


def missionvission_delete(request,pk):
    missionvission=Mission_and_Vission.objects.get(pk=pk)
    missionvission.delete()
    messages.success(request, 'Successfully delete')
    return redirect('missionvission-list')

# event

def event_list(request):
    event_list = Event.objects.all().order_by('-id')
    return render(request, 'dashboard/event/list.html', {'event_list':event_list})

def event_add(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event-list')
    else:
        form = EventForm()
    return render(request, 'dashboard/event/add.html', {'form':form})

def event_edit(request,pk):
    event = Event.objects.get(pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST,request.FILES,instance=event)
        if form.is_valid():
            form.save()
            return redirect('event-list') 
        else:
            return redirect('event-add')
    else:
        form = EventForm(instance=event)
    return render(request, 'dashboard/event/add.html', {'form':form})


def event_delete(request,pk):
    event=Event.objects.get(pk=pk)
    event.delete()
    messages.success(request, 'Successfully delete')
    return redirect('event-list')

# mediacoverage

def mediacoverage_list(request):
    mediacoverage_list = MediaCovarage.objects.all().order_by('-id')
    return render(request, 'dashboard/mediacoverage/list.html', {'mediacoverage_list':mediacoverage_list})

def mediacoverage_add(request):
    if request.method == 'POST':
        form = MediaCovarageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mediacoverage-list')
    else:
        form = MediaCovarageForm()
    return render(request, 'dashboard/mediacoverage/add.html', {'form':form})

def mediacoverage_edit(request,pk):
    mediacoverage = MediaCovarage.objects.get(pk=pk)
    if request.method == 'POST':
        form = MediaCovarageForm(request.POST,request.FILES,instance=mediacoverage)
        if form.is_valid():
            form.save()
            return redirect('mediacoverage-list') 
        else:
            return redirect('mediacoverage-add')
    else:
        form = MediaCovarageForm(instance=mediacoverage)
    return render(request, 'dashboard/mediacoverage/add.html', {'form':form})


def mediacoverage_delete(request,pk):
    mediacoverage=MediaCovarage.objects.get(pk=pk)
    mediacoverage.delete()
    messages.success(request, 'Successfully delete')
    return redirect('mediacoverage-list')

# bookingstudent

def bookingstudent_list(request):
    bookingstudent_list = BokingNow.objects.all().order_by('-id')
    return render(request, 'dashboard/BookingStudent/list.html', {'bookingstudent_list':bookingstudent_list})

def bookingstudent_add(request):
    if request.method == 'POST':
        form = BookingStudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bookingstudent-list')
    else:
        form = BookingStudentForm()
    return render(request, 'dashboard/BookingStudent/add.html', {'form':form})

def bookingstudent_edit(request,pk):
    bookingstudent = BokingNow.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookingStudentForm(request.POST,request.FILES,instance=bookingstudent)
        if form.is_valid():
            form.save()
            return redirect('bookingstudent-list') 
        else:
            return redirect('bookingstudent-add')
    else:
        form = BookingStudentForm(instance=bookingstudent)
    return render(request, 'dashboard/BookingStudent/add.html', {'form':form})


def bookingstudent_delete(request,pk):
    bookingstudent=BokingNow.objects.get(pk=pk)
    bookingstudent.delete()
    messages.success(request, 'Successfully delete')
    return redirect('bookingstudent-list')



# countdown

def countdown_list(request):
    countdown_list = Countdown.objects.all().order_by('-id')
    return render(request, 'dashboard/countdown/list.html', {'countdown_list':countdown_list})

def countdown_add(request):
    if request.method == 'POST':
        form = CountdownForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('countdown-list')
    else:
        form = CountdownForm()
    return render(request, 'dashboard/countdown/add.html', {'form':form})

def countdown_edit(request,pk):
    countdown = Countdown.objects.get(pk=pk)
    if request.method == 'POST':
        form = CountdownForm(request.POST,request.FILES,instance=countdown)
        if form.is_valid():
            form.save()
            return redirect('countdown-list') 
        else:
            return redirect('countdown-add')
    else:
        form = CountdownForm(instance=countdown)
    return render(request, 'dashboard/countdown/add.html', {'form':form})


def countdown_delete(request,pk):
    countdown=Countdown.objects.get(pk=pk)
    countdown.delete()
    messages.success(request, 'Successfully delete')
    return redirect('countdown-list')


# bkashpayment

def bkashpayment_list(request):
    bkashpayment_list = BkashPayment.objects.all().order_by('-id')
    return render(request, 'dashboard/bkashpayment/payment_list.html', {'bkashpayment_list':bkashpayment_list})

def bkashpayment_delete(request,pk):
    bkashpayment=BkashPayment.objects.get(pk=pk)
    bkashpayment.delete()
    messages.success(request, 'Successfully delete')
    return redirect('bkashpayment-list')


# userprofile

def userprofile_list(request):
    userprofile_list = Profile.objects.all().order_by('-id')
    return render(request, 'dashboard/userprofile/list.html', {'userprofile_list':userprofile_list})

def userprofile_add(request):
    if request.method == 'POST':
        form = UserprofileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('userprofile-list')
    else:
        form = UserprofileForm()
    return render(request, 'dashboard/userprofile/add.html', {'form':form})

def userprofile_edit(request,pk):
    userprofile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserprofileForm(request.POST,request.FILES,instance=userprofile)
        if form.is_valid():
            form.save()
            return redirect('userprofile-list') 
        else:
            return redirect('userprofile-add')
    else:
        form = UserprofileForm(instance=userprofile)
    return render(request, 'dashboard/userprofile/add.html', {'form':form})


def userprofile_delete(request,pk):
    userprofile=Profile.objects.get(pk=pk)
    userprofile.delete()
    messages.success(request, 'Successfully delete')
    return redirect('userprofile-list')

