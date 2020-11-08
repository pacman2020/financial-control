from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.products, name='products'),
    path('product/new/', views.new_product, name='new_product'),
    path('product/<int:pk>/', views.detail_product, name='detail_product'),
    path('product/<int:pk>/update', views.update_product, name='update_product'),
    path('product/<int:pk>/delete', views.delete_product, name='delete_product'),
]
