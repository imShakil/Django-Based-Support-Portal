from django.shortcuts import render

# Create your views here.

def profile(request, userName):
    return render(request, 'profile.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def tickets(request):
    return render(request, 'openticket.html')

def facultynstaff(request, id):
    return render(request, 'facultynstaff.html', {id:id})

