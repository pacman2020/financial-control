from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name_product = models.CharField(max_length=150)
    supplier_name = models.CharField(max_length=200)
    resale_value = models.DecimalField(max_digits=5, decimal_places=2)
    commercial_value = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.IntegerField()
    active = models.BooleanField(blank=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_product