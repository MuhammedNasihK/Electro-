from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm,ForgotEmailForm,ForgotOtpForm,NewPasswordForm
from django.contrib.auth import get_user_model,login as user_login,logout as user_logout
from django.contrib.auth.decorators import login_required
from .decorators import logout_required
from django.core.mail import send_mail
from django.conf import settings
import random,time


# Create your views here.

User = get_user_model()

@logout_required
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


@logout_required
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


@logout_required
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
            
            otp = str(random.randint(100000,999999))
            
            send_mail(
                subject = 'ELECTRO, OTP to reset password',
                message = f'Your OTP for reset password is {otp}.It expires in 2 minutes',
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [email],
                fail_silently = False
            )
            
            request.session['otp'] = otp
            request.session['email'] = email
            request.session['otp_time'] = time.time()

            return redirect('forgot_password_otp')

    form = ForgotEmailForm()
    return render(request,'forgot password email.html',{'form':form})


@logout_required
def forgot_password_otp(request):
    if 'otp' not in request.session:
        return redirect('forgot_password_email')
    
    if request.method == 'POST':
        form = ForgotOtpForm(request.POST)
        if form.is_valid():
            otp = form.get_otp()

            if time.time() - request.session['otp_time'] > 120:
                del request.session['otp']
                del request.session['otp_time']
                form.add_error(None,'OTP expired')
                return render(request,'forgot password otp.html',{'form':form,'otp_expired': True})

            session_otp = request.session.get('otp')

            if otp == session_otp:
                del request.session['otp']
                del request.session['otp_time']
                request.session['otp_verified'] = True
                return redirect('new_password')
            
            else:
                form.add_error(None,"Invalid OTP") 
                return render(request,'forgot password otp.html',{'form':form})

    form = ForgotOtpForm()
    return render(request,'forgot password otp.html',{'form':form})


@logout_required
def resend_otp(request):
    if 'email' not in request.session:
        return redirect('forgot_password_email')
    
    email = request.session['email']
    try:
        del request.session['otp']
    except KeyError:
        pass
    otp = str(random.randint(100000,999999))
    send_mail(
        subject = 'ELECTRO, OTP to reset password',
        message = f"Your OTP to reset password is {otp}.It expires in 2 minutes.",
        from_email = settings.EMAIL_HOST_USER,
        recipient_list = [email],
        fail_silently = False
    )

    request.session['otp'] = otp
    request.session['otp_time'] = time.time()
    return redirect('forgot_password_otp')


@logout_required
def new_password(request):
    if 'otp_verified' not in request.session:
        return redirect('email')
    if request.method == 'POST':
        form = NewPasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']

            email = request.session['email']
            del request.session['email']
            del request.session['otp_verified']

            user_data = User.objects.get(email=email)
            user_data.set_password(password)
            user_data.save()
            return redirect('login')
    else:
        form = NewPasswordForm()
        
    return render(request,'new password.html',{'form':form})