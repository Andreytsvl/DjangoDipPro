from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView

from products_app.models import Products
# from goods.utils import q_search

def catalog(request):
    products_app = Products.objects.all() #ORM -запрос

    context = {
        "title": "Home - Каталог",
        "products_app": products_app,

    }
    return render(request, "products_app/catalog.html", context)


def products(request):
    # product = Products.objects.get(slug=product_slug)
    #
    # context = {"product": product}

    return render(request, "products_app/products.html")


