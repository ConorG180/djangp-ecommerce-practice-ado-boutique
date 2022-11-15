from django.contrib import admin
from .models import Category, Product

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name"
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "sku",
        "name",
        "description",
        "price",
        "rating",
        "image_url",
        "image",
    )

    ordering = ("sku",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
