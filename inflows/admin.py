from django.contrib import admin
from .import models

@admin.register(models.Inflow)
class InflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'supplier', 'quantity')
    search_fields = ('product__name', 'supplier__name')
    list_filter = ('product', 'supplier')
    
search_fields = ('product__name', 'supplier__name')
list_filter = ('product', 'supplier')
