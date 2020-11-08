from product.models import Product
from django.db import models
from django.contrib.auth.models import User

class Sale(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ManyToManyField(Product)
    purchase_price = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(blank=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id.username
