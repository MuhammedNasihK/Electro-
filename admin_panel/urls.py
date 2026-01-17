from django.urls import path
from . import views

urlpatterns = [
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('admin_orders/',views.admin_orders,name='admin_orders'),
    path('admin_products/',views.admin_products,name='admin_products'),
    path('admin_users/',views.admin_users,name='admin_users'),
    path('admin_settings/',views.admin_settings,name='admin_settings'),
    path('admin_coupons/',views.admin_coupons,name='admin_coupons'),
    path('admin_banners/',views.admin_banners,name='admin_banners'),
    path('admin_add_products/',views.admin_add_products,name='admin_add_products'),
]