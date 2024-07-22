from django.urls import path
from products_app import views

app_name = 'products_app'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('products/', views.products, name='products'),
]