from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.

def sign_up(request):
    form = SignUpForm()

    return render(request,'sign up.html',{'form':form})

def login(request):
    return render(request,'login.html')

def wishlist(request):
    return render(request,'wishlist.html')

def profile(request):
    return render(request,'profile.html')

def forgot_password_email(request):
    return render(request,'forgot password email.html')

def forgot_password_otp(request):
    return render(request,'forgot password otp.html')

def new_password(request):
    return render(request,'new password.html')