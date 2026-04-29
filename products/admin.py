from django.contrib import admin
from .import models 

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'category', 'supplier')
    search_fields = ('name', 'brand__name', 'category__name', 'supplier__name')
    list_filter = ('brand', 'category', 'supplier')

# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'category')
    search_fields = ( 'brand__name', 'category__name', 'supplier__name')
    list_filter = ('brand', 'category')
