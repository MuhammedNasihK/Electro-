from django.shortcuts import render
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your views here.

def home(request):

    return render(request,'home.html')

def products(request):
    return render(request,'products.html')


def product_review(request):
    return render(request,'product review.html')

def cart(request):
    return render(request,'cart.html')

def payment(request):
    return render(request,'payment.html')

def orders(request):
    return render(request,'orders.html')

def checkout(request):
    return render(request,'checkout.html')

def about(request):
    return render(request,'about.html')