from django.contrib import admin
from .import models

@admin.register(models.Outflow)
class OutflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('product__title',)

