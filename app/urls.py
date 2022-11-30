from django.urls import path
from.views import home , specialistts

urlpatterns = [
    path('',home),
    path('specialistts/', specialistts),
]