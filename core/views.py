from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def menu(request):
    return render(request, 'menu.html')

def booking(request):
    return render(request, 'booking.html')

def login(request):
    return render(request, 'login.html')
