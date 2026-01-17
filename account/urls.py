from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/',views.sign_up,name='sign_up'),
    path('login/',views.login,name='login'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('profile/',views.profile,name='profile'),
    path('forgot_password_email/',views.forgot_password_email,name='forgot_password_email'),
    path('forgot_password_otp/',views.forgot_password_otp,name='forgot_password_otp'),
    path('new_password/',views.new_password,name='new_password'),
]