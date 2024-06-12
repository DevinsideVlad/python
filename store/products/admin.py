from django.contrib import admin

# Register your models here.
from products.models import ProductCategory, Product, ProductFilter




# admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductFilter)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name',)




