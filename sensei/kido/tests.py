from cgitb import html
from django.test import TestCase
from django.urls import reverse,resolve
from .views import home,about_us,contact_us

# Create your tests here.

class Viewstestcase(TestCase):
    
    def test_home(self):
        res= resolve(reverse('home'))
        response = self.client.get(reverse('home'))
        self.assertEqual(200,response.status_code)
        self.assertContains(response, 'have a lot features coming up later')
        self.assertTemplateUsed(response,'home.html')
    
    def test_about_us(self):
        res= resolve(reverse('about_us'))
        response = self.client.get(reverse('about_us'))
        self.assertEqual(200,response.status_code)
        self.assertContains(response, 'We are software company that')
        self.assertTemplateUsed(response,'aboutus.html')
    
    def test_home(self):
        res= resolve(reverse('contact_us'))
        response = self.client.get(reverse('contact_us'))
        self.assertEqual(200,response.status_code)
        self.assertContains(response, 'If you want to contact us')
        self.assertTemplateUsed(response,'contactus.html')
