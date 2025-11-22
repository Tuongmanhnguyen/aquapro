from django.contrib import admin
from .models import Product, Category  # <--- Import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)} # Auto-fill slug as you type name

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'price', 'category', 'in_stock') # <--- Add category to list
    search_fields = ('name', 'sku')
    list_filter = ('category',) # <--- Add filter sidebar