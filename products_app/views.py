from django.shortcuts import render, get_list_or_404
from django.http import Http404
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator
from products_app.models import Products
# from goods.utils import q_search

def catalog(request, category_id, page=1):
    if category_id == 5:
        products_app = Products.objects.all()
    else:
        products_app = get_list_or_404(Products.objects.filter(category__id=category_id)) #ORM -запрос
        # if not products_app.exists():
        #     raise Http404()

    paginator = Paginator(products_app, 3)
    current_page = paginator.page(page)

    context = {
        "title": "Home - Каталог",
        "products_app": current_page,
        "id_url":category_id,

    }
    return render(request, "products_app/catalog.html", context)


def products(request, product_slug=False, product_id=False):
    if product_id:
        product = Products.objects.get(id=product_id) #ORM

    else:
        product = Products.objects.get(slug=product_slug)
    context = {"product": product}

    return render(request, "products_app/products.html", context=context)


