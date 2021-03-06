from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    active = models.BooleanField(blank=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name