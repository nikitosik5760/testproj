from django.contrib import admin
from .models import Category, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name', )}


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'slug', 'price', 'created_at']
    list_filter = ['created_at']
    list_editable = ('price', )
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
