from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('orders/',views.admin_orders,name='admin_orders'),
    path('products/',views.admin_products,name='admin_products'),
    path('users/',views.admin_users,name='admin_users'),
    path('settings/',views.admin_settings,name='admin_settings'),
    path('coupons/',views.admin_coupons,name='admin_coupons'),
    path('banners/',views.admin_banners,name='admin_banners'),
    path('add_products/',views.admin_add_products,name='admin_add_products'),
    path('logout/',views.admin_logout,name='admin_logout'),
]