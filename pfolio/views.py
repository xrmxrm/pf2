from django.shortcuts import render

def home(request):
    return render(request, 'pfolio/home.html')
