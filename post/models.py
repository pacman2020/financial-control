from django.db import models
from django.contrib.auth.models import User
from task.models import Task
from employee.models import Employee
from django.utils import timezone

class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.task_id.name