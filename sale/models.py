from product.models import Product
from django.db import models
from django.contrib.auth.models import User

class Sale(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_price = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.IntegerField(blank=False)
    active = models.BooleanField(blank=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_id.name_product
