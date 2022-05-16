from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_item_render, name='create-item-render'),
    path('create_post/', views.create_item_post, name='create-item-post'),
    path('', views.read_items, name='read-inventory'),
    path('update/<uuid:yourUUIDFieldName>/', views.update_item, name='update-item'),
    path('delete/<uuid:yourUUIDFieldName>/', views.delete_item, name='delete-item'),
]