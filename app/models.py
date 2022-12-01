from django.db import models

class Specialistts(models.Model):
    fio = models.CharField(max_length=100)
    age = models.DateField()
    experrience = models.IntegerField()
    speciality = models.CharField(max_length=100)
