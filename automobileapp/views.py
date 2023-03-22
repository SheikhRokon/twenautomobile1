from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views.generic import View
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q 
from userapp.models import *

# Create your views here.

import requests, json

def get_ip_address(request):
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    uip = requests.get(f'http://ip-api.com/json/{ip}')
    response =json.loads(uip.content)

    status = response.get('status')
    query = response.get('query')
    country = response.get('country')
    city = response.get('city')
    regionName = response.get('regionName')

    if status != 'fail':
        UserIp.objects.create(user_ip=query,country=country,city=city,division=regionName)
    else:
        UserIp.objects.create(user_ip='traking not possible')
    return response

class HomePageListView(View):
    def get(self,request):
        banner = BannerSlider.objects.all()
        course = Course.objects.all()
        upcomming_course = UpcommingCourse.objects.all()
        our_partner = OurPartner.objects.all()
        course_categorie = CourseCategory.objects.all()
        testimonial = Testimonial.objects.all()
        intructor = OurInstructor.objects.all()[:4]
        fas =FREQUENTLY_ASKED_QUESTIONS.objects.all()
        certificates = Certificate.objects.all()
        ourAlumnus = OurAlumnus.objects.all()
        imagegallery = ImageGallery.objects.all()
        videoGallery = VideoGallery.objects.all()[:8]
        blogs = Blog.objects.all()[:8]
        course_type  = CourseType.objects.all()
        countdown = Countdown.objects.last()
        
        form = NewsLetterForm(request.POST)
        for_enquiery_form =ForEnquiryForm(request.POST)

        get_ip_address(request)

        context={
            'banner':banner,
            'course':course,
            'course_categorie':course_categorie,
            'upcomming_course':upcomming_course,
            'our_partner':our_partner,
            'testimonial':testimonial,
            'intructor':intructor,
            'fas':fas,
            'countdown':countdown,
            'certificates':certificates,
            'ourAlumnus':ourAlumnus,
            'imagegallery':imagegallery,
            'videoGallery':videoGallery,
            'blogs':blogs,
            'course_type':course_type,
            'form':form,
            'for_enquiery_form':for_enquiery_form,

        }
        
        return render(request, 'automobileapp/home.html', context)

    def post(self, request):
        for_enquiery_form =ForEnquiryForm(request.POST)
        form =NewsLetterForm(request.POST)
        if for_enquiery_form.is_valid():
            for_enquiery_form.save()
            messages.success(request, f'successfully submit')
            return redirect('home')

        if form.is_valid():
            form.save()
            messages.success(request, f'successfully submit')
            return redirect('home')
        else:
            form =NewsLetterForm()
            for_enquiery_form =ForEnquiryForm()
            
            return render(request,'automobileapp/home.html', {'form':form,'course_find_form':course_find_form, 'for_enquiery_form':for_enquiery_form})  


def blogs(request):

    blogs = Blog.objects.all()
    get_ip_address(request)
    context ={
        'blogs':blogs,
    }
    return render(request,'automobileapp/blogs.html',context)


def blogs_detail(request, pk):
    blogs = Blog.objects.get(pk=pk)

    form = BlogCommentForm()
    if request.method == 'POST':
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = BlogsComment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                blogs=blogs
            )
            comment.save()
            messages.success(request, f'successfully submit')
            return redirect('blog-detals', pk=pk)


    comments = BlogsComment.objects.filter(pk=pk)
    
    blogs.view_count = blogs.view_count + 1
    blogs.save()

    context = {
        "blogs": blogs,
        'comments':comments,
        'form':form
    }
    return render(request, "automobileapp/details/blogs-detail.html", context)


def course_categorie_detail(request, slug):
    course_categorie = CourseCategory.objects.get(slug=slug)

    context = {
        "course_categorie": course_categorie
    }
    return render(request, "automobileapp/details/course_categorie-detail.html", context)

def upcomming_course(request):
    course = UpcommingCourse.objects.all()
    context ={
        'course':course,
        
    }
    return render(request,'automobileapp/upcomming-course.html', context)

def upcomming_course_detail(request, slug):
    course = UpcommingCourse.objects.get(slug=slug)
    type_of_vehicles = TypeOfVehicles.objects.filter(course=course.id)

    context = {
        "course": course,
        'type_of_vehicles':type_of_vehicles,
    }
    return render(request, "automobileapp/details/up_course-detail.html", context)


def course(request):
    course = Course.objects.all()
    
    
    context ={
        'course':course,
        
    }
    return render(request,'automobileapp/course.html', context)


def course_detail(request, slug):
    course = Course.objects.get(slug=slug)
    type_of_vehicles = TypeOfVehicles.objects.filter(course=course.id)

    context = {
        "course": course,
        'type_of_vehicles':type_of_vehicles,
    }
    return render(request, "automobileapp/details/course-detail.html", context)

def course_search(request):
    query = request.GET['q']
    search_item = Q(title__icontains=query) | Q(course_price__icontains=query) | Q(course_categorie__title__icontains=query)
    course = Course.objects.filter(search_item)

    context ={
        'course' : course
    }
    return render(request,'automobileapp/search-course.html', context)


def CourseTypeFilter(request,pk):
    course_type  = CourseType.objects.get(pk=pk)   
    course = Course.objects.filter(course_type=course_type.id)

    context={
        'course':course
    }
    return render(request,'automobileapp/course.html', context)

def intructor(request):
    intructor = OurInstructor.objects.all()
    context ={
        'intructor':intructor
    }
    return render(request,'automobileapp/ourintructor.html', context)

def imageGallery(request):
    image_gallery = ImageGallery.objects.all()
    context ={
        'image_gallery':image_gallery
    }
    return render(request,'automobileapp/image-gallery.html', context)


def image_gallery_detail(request, slug):
    image_gallery = ImageGallery.objects.get(slug=slug)

    context = {
        "image_gallery": image_gallery
    }
    return render(request, "automobileapp/details/image_gallery-detail.html", context)


def videoGallery(request):
    video_gallery = VideoGallery.objects.all()
    context ={
        'video_gallery':video_gallery
    }
    return render(request,'automobileapp/video-gallery.html', context)

def notice(request):
    notice = Notice.objects.all()
    context ={
        'notice':notice
    }
    return render(request,'automobileapp/notice.html', context)

def director_message(request):
    director_message = DirectorMessage.objects.all()
    context ={
        'director_message':director_message
    }
    return render(request,'automobileapp/diractor_message.html', context)

def mission_vission(request):
    mission_vission = Mission_and_Vission.objects.all().order_by('-id')[:1]
    context ={
        'mission_vission':mission_vission
    }
    return render(request,'automobileapp/mission_vission.html', context)

def protfolio(request):

    return render(request,'automobileapp/protfolio.html')

def event(request):
    event = Event.objects.all()
    context ={
        'event':event
    }
    return render(request,'automobileapp/event.html', context)

def event_detail(request, slug):
    event = Event.objects.get(slug=slug)
    context = {
        "event": event
    }
    return render(request, "automobileapp/details/event-detail.html", context)

def review(request):
    review = Testimonial.objects.all()
    context ={
        'review':review
    }
    return render(request,'automobileapp/review.html', context)

def mediacover(request):
    mediacover = MediaCovarage.objects.all()
    context ={
        'mediacover':mediacover
    }
    return render(request,'automobileapp/mediacoverage.html', context)
    
    
def about(request):
    return render(request,'automobileapp/about.html')


def privacy_policy(request):
    return render(request,'automobileapp/privacy-policy.html')
    
    