"""Views"""
from django.shortcuts import render, redirect
from main.models import Dish
from main.models import Cart
from random import randint
from main.forms import Dish_in_shopcartForm
from django.contrib.auth.decorators import login_required
#from main.forms import DishForm


def get_base_context(request):
    """Main mneu"""
    menu = [
        {"link": "/", "text": "Главная"},
        {"link": "/menu", "text": "Меню"}
    ]
    if request.user.is_authenticated:
        menu.append({"link": "/logout", "text": "Выйти"})
    else:
        menu.append({"link": "/login", "text": "Войти"})
    return menu


def menu_page(request):
    """ Dishes page html"""
    base = get_base_context(request)
    data = {}
    if request.method == "POST":
        items2 = Dish.objects.filter(cart__user_id=228)
        data["in_cart"] = items2
    items = Dish.objects.all()
    data["menu"] = base
    data["items"] = items
    return render(request, "menu.html", data)

def add_dish(request, dish_id):
    item = Dish.objects.get(id=dish_id)
    try:
        a1 = Cart.objects.get(user_id=228)
    except Exception:
        a1 = Cart(user_id=228)
    a1.save()
    a1.dishes.add(item)
    a1.save()
    return redirect("/menu")



##@login_required()
def main_page(request):
    """Main page html"""
    base = get_base_context(request)
    data = {}
    data["menu"] = base
    return render(request, "main.html", data)



def kontakts_page(request):
    """ Kontakts page html"""

    data = {}

    return render(request, "kontakts.html", data)


def map_page(request):
    """Map Page"""
    data = {}
    return render(request, "map.html", data)
