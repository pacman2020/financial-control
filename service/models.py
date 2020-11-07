from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(blank=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name