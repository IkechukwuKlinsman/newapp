from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,'home.html')

def about_us(request):
    return render(request,'aboutus.html')

def contact_us(request):
    return render(request,'contactus.html')