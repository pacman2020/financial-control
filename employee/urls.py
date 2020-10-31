from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.employees, name='employees'),
    path('employee/new/', views.new_employee, name='new_employee'),
    path('employee/<int:pk>/', views.detail_employee, name='detail_employee'),
    path('employee/<int:pk>/update', views.update_employee, name='update_employee'),
    path('employee/<int:pk>/delete', views.delete_employee, name='delete_employee'),
]
