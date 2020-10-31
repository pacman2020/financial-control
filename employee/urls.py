from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.employees, name='employees'),
    # path('employee/new/', views.new_employee, name='new_employee'),
    path('employee/<int:pk>/', views.detail_employee, name='detail_employee'),
    # path('task/<int:pk>/update', views.update_task, name='update_task'),
    # path('task/<int:pk>/delete', views.delete_task, name='delete_task'),
]
