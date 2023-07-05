from django.contrib import admin
from .models import Category, Product

# Register your models here.


class ProductCategoryInline(admin.TabularInline):
    model = Product.category.through
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag_thumbnail')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('image_tag_thumbnail',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'quantity', 'price')
    inlines = (ProductCategoryInline,)
