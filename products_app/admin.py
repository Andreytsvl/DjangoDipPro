from django.contrib import admin
from products_app.models import Categories, Recipe_status, Storage_conditions, Price_category, Products

admin.site.register(Categories)
admin.site.register(Recipe_status)
admin.site.register(Storage_conditions)
admin.site.register(Price_category)
admin.site.register(Products)
