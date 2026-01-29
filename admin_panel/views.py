from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .decorators import admin_login_required


# Create your views here.

User = get_user_model()

@admin_login_required
def admin_dashboard(request):
    return render(request,'admin dashboard.html')

@admin_login_required
def admin_orders(request):
    return render(request,'admin orders.html')

@admin_login_required
def admin_products(request):
    return render(request,'admin products.html')

@admin_login_required
def admin_users(request):
    user_data = User.objects.filter(is_superuser=False)
    return render(request,'admin users.html',{'user_data':user_data})

@admin_login_required
def admin_settings(request):
    return render(request,'admin_settings.html')

@admin_login_required
def admin_coupons(request):
    return render(request,'admin_coupons.html')

@admin_login_required
def admin_banners(request):
    return render(request,'admin_banners.html')

@admin_login_required
def admin_add_products(request):
    return render(request,'admin_add_products.html')

def admin_logout(request):
    del request.session['admin_id']
    return redirect('home')

def add_user(request):
    return render(request)

def edit_user(request):
    return render(request)