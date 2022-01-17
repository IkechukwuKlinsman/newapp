from django.urls import path
from .views import home,about_us,contact_us

urlpatterns = [
    path('home/',home,name='home'),
    path('aboutus/',about_us,name='about_us'),
    path('contactus/',contact_us,name='contact_us'),
    
]