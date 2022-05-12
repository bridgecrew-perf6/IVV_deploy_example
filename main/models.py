"""Models"""
from django.db import models

class Dish(models.Model):
    """ Model of dishes in my menu"""
    name = models.TextField()
    price = models.IntegerField()
    weight = models.IntegerField()
    description = models.TextField()

class Cart(models.Model):
    """ Model of dishes in my menu"""
    user_id = models.IntegerField()
    dishes = models.ManyToManyField(Dish)
    ##amount = models.IntegerField()
