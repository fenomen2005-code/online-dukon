from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}

       
        extra_context['total_products'] = Product.objects.count()

        return super().changelist_view(request, extra_context=extra_context)