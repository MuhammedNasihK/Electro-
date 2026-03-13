from django.db import models
from admin_panel.models import *
from django.conf import settings


class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='wishlist')
    product_variant = models.ForeignKey('admin_panel.ProductVariant',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user','product_variant')

    def __str__(self):
        return f"{self.user.email} - {self.product_variant.product.name}"

