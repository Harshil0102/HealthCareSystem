from django.shortcuts import render, redirect
from accounts.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'authentication/password_reset.html'
    email_template_name = 'authentication/password_reset_email.html'
    subject_template_name = 'authentication/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'authentication/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')


def handleSignup(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        phone_number=request.POST['phone_number']
        role=request.POST['role']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password == confirm_password:                    
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('/accounts/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/accounts/signup')
            else:
                s = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,phone_number=phone_number,role=role,password=password )
                s.save()  
                messages.success(request,"Registration successfully")   
                return redirect('/accounts/login')
        else:
            messages.error(request, 'Password not match...')
            return redirect('/accounts/signup')

    
    return render(request, 'authentication/register.html')
   
    
def handleLogin(request):
    if request.method=='POST':
         # Get the post parameters
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request, "Successfully Logged In")
            request.session['uid']=username
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/accounts/login/")
        
    return render(request, 'authentication/login.html')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    # del request.session['uid']
    return redirect('/')


