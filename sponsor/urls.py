from django.contrib import admin
from django.urls import path

from sponsor import views

urlpatterns = [
    path('', views.sponsor_list, name='sponsor_list'),
    path('sponsor_upload/', views.sponsor_upload, name="sponsor_upload"),
    path('sponsor_delete/<int:pk>/', views.sponsor_delete, name='sponsor_delete'),
    # path('sponsor_update/<int:pk>/', views.sponsor_update, name='sponsor_update'),
    # path('sponsor_detail/<int:pk>/', views.sponsor_detail, name='sponsor_detail'),
    # path('sponsor_list_search/<int:pk>/', views.sponsor_list_search, name='sponsor_list_search'),
]
