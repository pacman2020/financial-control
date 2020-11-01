from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_post , name='posts'),
    path('post/new/', views.new_post, name='new_post'),
    path('post/<int:pk>/', views.detail_post, name='detail_post'),
    # path('employee/<int:pk>/update', views.update_employee, name='update_employee'),
    # path('employee/<int:pk>/delete', views.delete_employee, name='delete_employee'),
]
