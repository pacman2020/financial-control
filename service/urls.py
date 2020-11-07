from django.urls import path
from . import views

urlpatterns = [
    path('service/', views.services, name='services'),
    path('service/new/', views.new_service, name='new_service'),
    path('service/<int:pk>/', views.detail_service, name='detail_service'),
    path('service/<int:pk>/update', views.update_service, name='update_service'),
    path('service/<int:pk>/delete', views.delete_service, name='delete_service'),
]
