from django.shortcuts import render
from .models import *
def home(request):
    return render(request, 'index.html')

def specialistts(request):

    return render(request, 'specialistts.html')
def about(request):
    return render(request, 'About us.html')
def price(request):
    return render(request, 'price.html')


