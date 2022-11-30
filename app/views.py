from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def specialistts(request):
    return render(request, 'specialistts.html')