from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.tasks, name='tasks'),
    path('task/<int:pk>/', views.detail_task, name='detail_task'),
]
