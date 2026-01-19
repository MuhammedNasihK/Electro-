from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth import get_user_model

# Create your views here.


User = get_user_model()

def sign_up(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
           User.objects.create_user(
               username = form.cleaned_data['username'],
               email = form.cleaned_data['email'],
               phone = form.cleaned_data['phone'],
               password = form.cleaned_data['password']
           ) 

    else:
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