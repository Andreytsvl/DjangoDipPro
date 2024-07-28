from django.contrib import admin
from products_app.models import Categories, Recipe_status, Storage_conditions, Price_category, Products

#admin.site.register(Categories)
admin.site.register(Recipe_status)
admin.site.register(Storage_conditions)
admin.site.register(Price_category)
#admin.site.register(Products)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
#     list_display = ["name", "quantity", "price", "discount"]
#     list_editable = ["discount",]
#     search_fields = ["name", "description"]
#     list_filter = ["discount", "quantity", "category"]
#     fields = [
#         "name",
#         "category",
#         "slug",
#         "description",
#         "image",
#         ("price", "discount"),
#         "quantity",
#   ]

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):

    list_display = ["name", "id"]