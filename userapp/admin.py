from django.contrib import admin
from .models import *

admin.site.site_header = "TWEEN Automobile School"
admin.site.site_title = "TWEEN Automobile School"
admin.site.index_title = "TWEEN Automobile School"


# Register your models here.
admin.site.register(ConductData)
admin.site.register(User)
admin.site.register(Career)
admin.site.register(Profile)
admin.site.register(JobApplication)
admin.site.register(UserIp)