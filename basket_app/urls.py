from django.urls import path
from basket_app import views

app_name = 'basket_app'

urlpatterns = [
    path('basket_add/<slug:product_slug>/', views.basket_add, name='basket_add'),
    path('basket_change/<slug:product_slug>/', views.basket_change, name='basket_change'),
    path('basket_remove/<slug:product_slug>/', views.basket_remove, name='basket_remove'),
]