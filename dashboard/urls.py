from django.urls import path
from .views import *
urlpatterns = [
    path('debcukbkcdv/dashboard/home', dashboard_home, name='dashboard'),

    #visitor
    path('dashboard/today-visitor-list/', today_visitor_list, name='today-visitor-list'),
    path('dashboard/visitor-list/', visitor_list, name='visitor-list'),
    
    path('dashboard/unique-visitor-list/', unique_visitor_list, name='uniquevisitor-list'),
    path('dashboard/today/unique/visitor/list/', today_unique_visitor_list, name='today_unique_visitor-list'),
    
    path('dashboard/visitor_edit/<pk>',visitor_edit, name='visitor-edit'),
    path('dashboard/visitor_delete/<pk>/',visitor_delete, name='visitor-delete'),

    #career 
    path('dashboard/career-list/', career_list, name='career-list'),
    path('dashboard/career-add', career_add, name='career-add'),
    path('dashboard/career_edit/<pk>',career_edit, name='career-edit'),
    path('dashboard/career_delete/<pk>/',career_delete, name='career-delete'),

    #jobapplication 
    path('dashboard/jobapplication-list/', jobapplication_list, name='jobapplication-list'),
    path('dashboard/jobapplication-add', jobapplication_add, name='jobapplication-add'),
    path('dashboard/jobapplication_edit/<pk>',jobapplication_edit, name='jobapplication-edit'),
    path('dashboard/jobapplication_delete/<pk>/',jobapplication_delete, name='jobapplication-delete'),


    #forenquiry 
    path('dashboard/forenquiry-list/', forenquiry_list, name='forenquiry-list'),
    path('dashboard/forenquiry-add/', forenquiry_add, name='forenquiry-add'),
    path('dashboard/forenquiry_edit/<pk>',forenquiry_edit, name='forenquiry-edit'),
    path('dashboard/forenquiry_delete/<pk>/',forenquiry_delete, name='forenquiry-delete'),

    #banner 
    path('dashboard/banner-list/', banner_list, name='banner-list'),
    path('dashboard/banner-add/', banner_add, name='banner-add'),
    path('dashboard/banner_edit/<pk>',banner_edit, name='banner-edit'),
    path('dashboard/banner_delete/<pk>/',banner_delete, name='banner-delete'),

    #coursecategory 
    path('dashboard/coursecategory-list/', coursecategory_list, name='coursecategory-list'),
    path('dashboard/coursecategory-add/', coursecategory_add, name='coursecategory-add'),
    path('dashboard/coursecategory_edit/<pk>',coursecategory_edit, name='coursecategory-edit'),
    path('dashboard/coursecategory_delete/<pk>/',coursecategory_delete, name='coursecategory-delete'),
    
    #typeofvehicles 
    path('dashboard/typeofvehicles-list/', typeofvehicles_list, name='typeofvehicles-list'),
    path('dashboard/typeofvehicles-add/', typeofvehicles_add, name='typeofvehicles-add'),
    path('dashboard/typeofvehicles_edit/<pk>',typeofvehicles_edit, name='typeofvehicles-edit'),
    path('dashboard/typeofvehicles_delete/<pk>/',typeofvehicles_delete, name='typeofvehicles-delete'),

    #coursetype 
    path('dashboard/coursetype-list/', coursetype_list, name='coursetype-list'),
    path('dashboard/coursetype-add/', coursetype_add, name='coursetype-add'),
    path('dashboard/coursetype_edit/<pk>',coursetype_edit, name='coursetype-edit'),
    path('dashboard/coursetype_delete/<pk>/',coursetype_delete, name='coursetype-delete'),

    #course 
    path('dashboard/course-list/', course_list, name='course-list'),
    path('dashboard/course-add/', course_add, name='course-add'),
    path('dashboard/course_edit/<pk>',course_edit, name='course-edit'),
    path('dashboard/course_delete/<pk>/',course_delete, name='course-delete'),
    
    #upcomingcourse 
    path('dashboard/upcomingcourse-list/', upcomingcourse_list, name='upcomingcourse-list'),
    path('dashboard/upcomingcourse-add/', upcomingcourse_add, name='upcomingcourse-add'),
    path('dashboard/upcomingcourse_edit/<pk>',upcomingcourse_edit, name='upcomingcourse-edit'),
    path('dashboard/upcomingcourse_delete/<pk>/',upcomingcourse_delete, name='upcomingcourse-delete'),
    
    #alumnus 
    path('dashboard/alumnus-list/', alumnus_list, name='alumnus-list'),
    path('dashboard/alumnus-add/', alumnus_add, name='alumnus-add'),
    path('dashboard/alumnus_edit/<pk>',alumnus_edit, name='alumnus-edit'),
    path('dashboard/alumnus_delete/<pk>/',alumnus_delete, name='alumnus-delete'),

    #testimonial 
    path('dashboard/testimonial-list/', testimonial_list, name='testimonial-list'),
    path('dashboard/testimonial-add/', testimonial_add, name='testimonial-add'),
    path('dashboard/testimonial_edit/<pk>',testimonial_edit, name='testimonial-edit'),
    path('dashboard/testimonial_delete/<pk>/',testimonial_delete, name='testimonial-delete'),

    #instructor 
    path('dashboard/instructor-list/', instructor_list, name='instructor-list'),
    path('dashboard/instructor-add/', instructor_add, name='instructor-add'),
    path('dashboard/instructor_edit/<pk>',instructor_edit, name='instructor-edit'),
    path('dashboard/instructor_delete/<pk>/',instructor_delete, name='instructor-delete'),

    #fqa 
    path('dashboard/fqa-list/', fqa_list, name='fqa-list'),
    path('dashboard/fqa-add/', fqa_add, name='fqa-add'),
    path('dashboard/fqa_edit/<pk>',fqa_edit, name='fqa-edit'),
    path('dashboard/fqa_delete/<pk>/',fqa_delete, name='fqa-delete'),

    #certificate 
    path('dashboard/certificate-list/', certificate_list, name='certificate-list'),
    path('dashboard/certificate-add/', certificate_add, name='certificate-add'),
    path('dashboard/certificate_edit/<pk>',certificate_edit, name='certificate-edit'),
    path('dashboard/certificate_delete/<pk>/',certificate_delete, name='certificate-delete'),

    #imagegallery 
    path('dashboard/imagegallery-list/', imagegallery_list, name='imagegallery-list'),
    path('dashboard/imagegallery-add/', imagegallery_add, name='imagegallery-add'),
    path('dashboard/imagegallery_edit/<pk>',imagegallery_edit, name='imagegallery-edit'),
    path('dashboard/imagegallery_delete/<pk>/',imagegallery_delete, name='imagegallery-delete'),

    #videogallery 
    path('dashboard/videogallery-list/', videogallery_list, name='videogallery-list'),
    path('dashboard/videogallery-add/', videogallery_add, name='videogallery-add'),
    path('dashboard/videogallery_edit/<pk>',videogallery_edit, name='videogallery-edit'),
    path('dashboard/videogallery_delete/<pk>/',videogallery_delete, name='videogallery-delete'),

    #blog 
    path('dashboard/blog-list/', blog_list, name='blog-list'),
    path('dashboard/blog-add/', blog_add, name='blog-add'),
    path('dashboard/blog_edit/<pk>',blog_edit, name='blog-edit'),
    path('dashboard/blog_delete/<pk>/',blog_delete, name='blog-delete'),
    
    #blogcomments 
    path('dashboard/blogcomments-list/', blogcomments_list, name='blogcomments-list'),
    path('dashboard/blogcomments-add/', blogcomments_add, name='blogcomments-add'),
    path('dashboard/blogcomments_edit/<pk>',blogcomments_edit, name='blogcomments-edit'),
    path('dashboard/blogcomments_delete/<pk>/',blogcomments_delete, name='blogcomments-delete'),

    #newsletter 
    path('dashboard/newsletter-list/', newsletter_list, name='newsletter-list'),
    path('dashboard/newsletter-add/', newsletter_add, name='newsletter-add'),
    path('dashboard/newsletter_edit/<pk>',newsletter_edit, name='newsletter-edit'),
    path('dashboard/newsletter_delete/<pk>/',newsletter_delete, name='newsletter-delete'),
    
    #notice 
    path('dashboard/notice-list/', notice_list, name='notice-list'),
    path('dashboard/notice-add/', notice_add, name='notice-add'),
    path('dashboard/notice_edit/<pk>',notice_edit, name='notice-edit'),
    path('dashboard/notice_delete/<pk>/',notice_delete, name='notice-delete'),

    #directormessage 
    path('dashboard/directormessage-list/', directormessage_list, name='directormessage-list'),
    path('dashboard/directormessage-add/', directormessage_add, name='directormessage-add'),
    path('dashboard/directormessage_edit/<pk>',directormessage_edit, name='directormessage-edit'),
    path('dashboard/directormessage_delete/<pk>/',directormessage_delete, name='directormessage-delete'),

    #missionvission 
    path('dashboard/missionvission-list/', missionvission_list, name='missionvission-list'),
    path('dashboard/missionvission-add/', missionvission_add, name='missionvission-add'),
    path('dashboard/missionvission_edit/<pk>',missionvission_edit, name='missionvission-edit'),
    path('dashboard/missionvission_delete/<pk>/',missionvission_delete, name='missionvission-delete'),

    #event 
    path('dashboard/event-list/', event_list, name='event-list'),
    path('dashboard/event-add/', event_add, name='event-add'),
    path('dashboard/event_edit/<pk>',event_edit, name='event-edit'),
    path('dashboard/event_delete/<pk>/',event_delete, name='event-delete'),

    #mediacoverage 
    path('dashboard/mediacoverage-list/', mediacoverage_list, name='mediacoverage-list'),
    path('dashboard/mediacoverage-add/', mediacoverage_add, name='mediacoverage-add'),
    path('dashboard/mediacoverage_edit/<pk>',mediacoverage_edit, name='mediacoverage-edit'),
    path('dashboard/mediacoverage_delete/<pk>/',mediacoverage_delete, name='mediacoverage-delete'),

    #countdown 
    path('dashboard/countdown-list/', countdown_list, name='countdown-list'),
    path('dashboard/countdown-add/', countdown_add, name='countdown-add'),
    path('dashboard/countdown_edit/<pk>',countdown_edit, name='countdown-edit'),
    path('dashboard/countdown_delete/<pk>/',countdown_delete, name='countdown-delete'),


    #bookingstudent 
    path('dashboard/bookingstudent-list/', bookingstudent_list, name='bookingstudent-list'),
    path('dashboard/bookingstudent-add/', bookingstudent_add, name='bookingstudent-add'),
    path('dashboard/bookingstudent_edit/<pk>',bookingstudent_edit, name='bookingstudent-edit'),
    path('dashboard/bookingstudent_delete/<pk>/',bookingstudent_delete, name='bookingstudent-delete'),

    #bkashpayment 
    path('dashboard/bkashpayment-list/', bkashpayment_list, name='bkashpayment-list'),
    path('dashboard/bkashpayment_delete/<pk>/',bkashpayment_delete, name='bkashpayment-delete'),
    

    
    #userprofile 
    path('dashboard/userprofile-list/', userprofile_list, name='userprofile-list'),
    path('dashboard/userprofile-add/', userprofile_add, name='userprofile-add'),
    path('dashboard/userprofile_edit/<pk>',userprofile_edit, name='userprofile-edit'),
    path('dashboard/userprofile_delete/<pk>/',userprofile_delete, name='userprofile-delete'),
    
]