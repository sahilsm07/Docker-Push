from django.db import models

# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=30)
    car_company = models.CharField(max_length=30)
    total_model_of_cars = models.IntegerField()

    def __str__(self):
        return self.car_name


