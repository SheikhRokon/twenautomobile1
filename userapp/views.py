from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
UserModel = User
 

# Create your views here.
def register(request):
    if request.method =='POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')      
            messages.success(request,f'Account created for {username}! You are now able to login')
            return redirect('login')
    else:
        form =RegisterForm()
    return render(request, 'userapp/register.html',{'form':form})

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user=form.save(commit=False)
#             user.is_active=False
#             user.save()
#             current_site = get_current_site(request)
#             mail_subject = 'Activate Your Account'
#             message = render_to_string('userapp/email_template.html', {
#                 'user':user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token' : default_token_generator.make_token(user),
#             })
#             send_mail=form.cleaned_data.get('email')
#             email=EmailMessage(mail_subject, message, to=[send_mail])
#             email.send()
#             messages.success(request, 'Successfully Created Account')
#             messages.info(request, 'Activate Your Account from the mail you provided')
#             return redirect('login')
#     else:
#         form = RegisterForm()
#     return render(request, 'userapp/register.html', {'form':form})

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your account is activated now, you can now log in")
        return redirect('login')
    else:
        messages.warning(request, "Activation link is invalid")
        return redirect('register')




@login_required
def profile(request):
    return render(request, 'userapp/profile.html')

@login_required
def profileupdate(request):
    if request.method == 'POST':
        u_form = UpdateRegisterForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UpdateRegisterForm(instance=request.user)
        p_form = UpdateProfileForm(instance=request.user.profile)

    context = {

        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'userapp/profileupdate.html', context)



def contact(request):
    form = Contact_Form(request.POST)
    if request.method == 'POST':
        form = Contact_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'successfully submit')
            return redirect('contact')
        else:
            form =Contact_Form()
            return render(request,'userapp/contact.html', {'form':form})  
    context={
        'form':form
    }
    return render(request, 'userapp/contact.html',context)

from datetime import datetime,timedelta

def career(request):
    careers = Career.objects.filter(active_status=True,end_date__gt = datetime.now())
    context={
        'careers':careers
    }
    return render(request, 'userapp/career.html',context)

def careerdetails(request,slug):
    careers =Career.objects.get(slug=slug)
    form =JobApplicationForm()
    if request.method == 'POST':
        form =JobApplicationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Submit Your Application')
            return redirect('career')
    context={
        'careers':careers,
        'form':form
    }
    return render(request, 'userapp/careerdetails.html',context)


    