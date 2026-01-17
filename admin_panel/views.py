from django.shortcuts import render

# Create your views here.

def admin_dashboard(request):
    return render(request,'admin dashboard.html')

def admin_orders(request):
    return render(request,'admin orders.html')

def admin_products(request):
    return render(request,'admin products.html')

def admin_users(request):
    return render(request,'admin users.html')

def admin_settings(request):
    return render(request,'admin_settings.html')

def admin_coupons(request):
    return render(request,'admin_coupons.html')

def admin_banners(request):
    return render(request,'admin_banners.html')

def admin_add_products(request):
    return render(request,'admin_add_products.html')