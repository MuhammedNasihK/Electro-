
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('product_review/',views.product_review,name='product_review'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('orders/',views.orders,name='orders'),
    path('payment/',views.payment,name='payment'),
    path('about/',views.about,name='about'),
]