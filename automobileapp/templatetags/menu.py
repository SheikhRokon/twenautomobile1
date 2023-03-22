from django import template
from automobileapp.models import *

register = template.Library()

@register.filter
def courses(request):
    return Course.objects.filter()