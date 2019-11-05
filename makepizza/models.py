from django.db import models

class Topping(models.Model):
    meat = models.CharField(max_length=50)
    vegetable = models.CharField(max_length=50)

    def __str__(self):
        return self.meat
        return self.vegetable 

class Sauce(models.Model):
    sauce = models.CharField(max_length=50)

    def __str__(self):
        return self.sauce

class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)
    pizza_sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE, null=True)

# Create your models here.
