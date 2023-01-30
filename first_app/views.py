from django.shortcuts import render
from .models import Car
from django.shortcuts import render
from .models import Car
from .serializer import CarSerializer
from rest_framework import viewsets

# Create your views here.
class CarViewset(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer