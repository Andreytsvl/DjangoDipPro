from django.http import JsonResponse
from django.shortcuts import redirect, render
from basket_app.models import Basket
from products_app.models import Products
from django.template.loader import render_to_string
from basket_app.utils import get_user_baskets

def basket_add(request):

    product_id = request.POST.get("product_id")
    product = Products.objects.get(id=product_id)#проблема

    if request.user.is_authenticated:
        baskets = Basket.objects.filter(user=request.user, product=product)

        if baskets.exists():
            basket = baskets.first()
            if basket:
                basket.quantity += 1
                basket.save()
        else:
            Basket.objects.create(user=request.user, product=product, quantity=1)

    user_basket = get_user_baskets(request)
    basket_items_html = render_to_string(
        "basket/includes/included_basket.html", {"basket": user_basket}, request=request)

    response_data = {
        "message": "Товар добавлен в корзину",
        "cart_items_html": basket_items_html,
    }

    return JsonResponse(response_data)


def basket_change(request, product_slug):

    pass

def basket_remove(request):
    basket_id = request.POST.get("basket_id")

    basket = Basket.objects.get(id=basket_id)#проблема
    quantity = basket.quantity
    basket.delete()

    user_basket = get_user_baskets(request)
    basket_items_html = render_to_string(
        "baskets/includes/included_basket.html", {"baskets": user_basket}, request=request)

    response_data = {
        "message": "Товар удален",
        "basket_items_html": basket_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)

