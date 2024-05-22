from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_object, name='create_object'),
    path('edit/<int:pk>/', views.edit_object, name='edit_object'),
    path('delete/<int:pk>/', views.delete_object, name='delete_object'),
]