from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm,ForgotEmailForm
from django.contrib.auth import get_user_model,login as user_login,logout as user_logout
from django.contrib.auth.decorators import login_required
import random

# Create your views here.


User = get_user_model()


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
           User.objects.create_user(
               username = form.cleaned_data['username'],
               email = form.cleaned_data['email'],
               password = form.cleaned_data['password']
           )
           return redirect('login') 

    else:
        form = SignUpForm()

    return render(request,'sign up.html',{'form':form})

def login(request):

    if request.user.is_authenticated:
        return redirect('home')
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user_data = User.objects.get(email=email)
            except User.DoesNotExist:
                form.add_error(None,'User not found')
                return render(request,'login.html',{'form':form})
            
            password = form.cleaned_data['password']

            if user_data.check_password(password):

                if user_data.is_active == False:
                    form.add_error(None,'Account is disabled')
                    return render(request,'login',{'form':form})
                
                if user_data.is_superuser == True:
                    request.session['admin_id'] = user_data.id
                    request.session.set_expiry(0)
                    return redirect('admin_dashboard')
                
                user_login(request,user_data)
                return redirect('home')
            
            else:
                form.add_error('password','Incorrect password')
                return render(request,'login.html',{'form':form})
           
   
    return render(request,'login.html',{'form':form})

@login_required
def logout(request):
    user_logout(request)
    return redirect('home')

def wishlist(request):
    return render(request,'wishlist.html')

def profile(request):
    return render(request,'profile.html')

def forgot_password_email(request):
    if request.method == 'POST':
        form = ForgotEmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user_data = User.objects.get(email=email)
            except User.DoesNotExist:
                form.add_error(None,'User Not Exist')
                return render(request,'forgot password email.html',{'form':form})
            
            otp = random.randint(000000,999999)
            

    form = ForgotEmailForm()
    return render(request,'forgot password email.html',{'form':form})

def forgot_password_otp(request):
    return render(request,'forgot password otp.html')

def new_password(request):
    return render(request,'new password.html')