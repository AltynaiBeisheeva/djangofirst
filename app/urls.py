from django.urls import path
from.views import home , specialistts , about , price

urlpatterns = [
    path('',home),
    path('specialistts/', specialistts),
    path('About us/', about),
    path('price/', price),
]