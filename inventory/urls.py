from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_item, name='create-item'),
    path('', views.read_items, name='read-inventory'),
    path('update/<uuid:yourUUIDFieldName>/', views.update_item, name='update-item'),
    path('delete/<uuid:yourUUIDFieldName>/', views.delete_item, name='delete-item'),
    path('deleted/', views.deleted_items, name='view-deleted'),
    path('revert/<uuid:yourUUIDFieldName>/', views.revert_deleted, name='revert-item')
]