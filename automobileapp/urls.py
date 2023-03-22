from django.urls import path
from .views import *
urlpatterns = [
    path('', HomePageListView.as_view(), name='home'),
    path('course', course, name='course'),
    path('instructor', intructor, name='instructor'),
    path('image-gallery', imageGallery, name='image-gallery'),
    path('video-gallery', videoGallery, name='video-gallery'),
    path('notice', notice, name='notice'),
    path('director_message',director_message, name='director_message'),
    path('mission_vission',mission_vission, name='mission-vission'),
    path('protfolio',protfolio, name='protfolio'),
    path('event',event, name='event'),
    path('review',review, name='review'),
    path('mediacover',mediacover, name='mediacover'),

    #details
    path('blog-details/<pk>/',blogs_detail, name='blog-detals'),
    path('category-details/<slug>',course_categorie_detail, name='category-detals'),
    path('event-details/<slug>',event_detail, name='event-detals'),
    path('image_gallery-details/<slug>',image_gallery_detail, name='image-gallery-detals'),
    path('course-details/<slug>',course_detail, name='course-detals'),
    path('upcomming-course/',upcomming_course, name='upcomming-course'),
    path('upcomming-course-details/<slug>',upcomming_course_detail, name='upcomming-course-detals'),
    path('course-type/<pk>',CourseTypeFilter, name='course-type'),
    path('course-search/',course_search, name = 'search'),
    path('about/',about, name = 'about'),
    path('blogs/',blogs, name = 'blogs'),
    path('privacy-policy/',privacy_policy, name ='privacy-policy'),
]