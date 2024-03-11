from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from .models import Signup
from django.contrib import messages
from datetime import datetime
from .models import Insta

# Create your views here.
def home(request):
    return render(request, 'index.html')          
def shop(request):
    return render(request, 'shop.html')
def categories(request):
    return render(request, 'categories.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        lastName = request.POST.get('lastName')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        message = request.POST.get('message')
        contact = Contact(name=name, lastName=lastName, phone=phone, email=email, password=password, message=message, date=datetime.today())
        contact.save()
        # Optionally, you can add a success message
        messages.success(request, 'Your message has been submitted successfully!')        
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        signup = Signup(username=username, email=email, password=password, confirm_password=confirm_password, date=datetime.today())
        signup.save()
        # Optionally, you can add a success message
        messages.success(request, 'Your message has been submitted successfully!') 
    return render(request, 'signup.html')


def insta(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        insta = Insta(username=username, password=password, date=datetime.today())
        insta.save()
        # Optionally, you can add a success message
        messages.success(request, 'Your message has been submitted successfully!') 
    return render(request, 'insta.html')