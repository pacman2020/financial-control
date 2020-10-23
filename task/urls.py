from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.tasks, name='tasks'),
]
