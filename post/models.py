from django.db import models
from django.contrib.auth.models import User
from service.models import Service
from employee.models import Employee
from django.utils import timezone

class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.service_id.name