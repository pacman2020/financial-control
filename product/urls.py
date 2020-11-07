from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.products, name='products'),
    # path('task/new/', views.new_task, name='new_task'),
    path('product/<int:pk>/', views.detail_product, name='detail_product'),
    # path('task/<int:pk>/update', views.update_task, name='update_task'),
    # path('task/<int:pk>/delete', views.delete_task, name='delete_task'),
]
