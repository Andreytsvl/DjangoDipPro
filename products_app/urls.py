from django.urls import path
from products_app import views

app_name = 'products_app'

urlpatterns = [
    path('<int:category_id>/', views.catalog, name='index'),
    path('<int:category_id>/<int:page>/', views.catalog, name='index'),
    path('products/<int:product_id>/', views.products, name='products'),
    path('products/<slug:product_slug>/', views.products, name='products'),

]