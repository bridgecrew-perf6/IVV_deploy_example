""" Forms """
from django import forms

class DishForm(forms.Form):
    """ Form of dishes in my menu"""
    name = forms.CharField()
    price = forms.IntegerField()
    weight = forms.IntegerField()
    description = forms.CharField()

class Dish_in_shopcartForm(forms.Form):
    """ Form of dishes in my menu"""
    name = forms.CharField()
    price = forms.IntegerField()
