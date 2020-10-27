from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.tasks, name='tasks'),
    path('task/new/', views.new_task, name='new_task'),
    path('task/<int:pk>/', views.detail_task, name='detail_task'),
    path('task/<int:pk>/update', views.update_task, name='update_task'),
    path('task/<int:pk>/delete', views.delete_task, name='delete_task'),
]
