from django.db import models

class Outflow(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT, related_name='outflows')
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name = 'Outflow'
        ordering = ['-created_at']
    
    
    def __str__(self):
        return str(self.description)
