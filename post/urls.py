from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_post , name='posts'),
    path('post/new/', views.new_post, name='new_post'),
    path('post/<int:pk>/', views.detail_post, name='detail_post'),
    path('post/<int:pk>/update', views.update_post, name='update_post'),
    path('post/<int:pk>/delete', views.delete_post, name='delete_post'),
]
