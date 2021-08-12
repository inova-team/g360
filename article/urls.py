from django.contrib import admin
from django.urls import path
from article import views

urlpatterns = [
    path('article_upload/', views.article_upload, name="article_upload"),
    path('article_delete/<int:pk>/', views.article_delete, name='article_delete'),
    path('article_update/<int:pk>/', views.article_update, name='article_update'),
    path('article_detail/<int:pk>/', views.article_detail, name='article_detail'),
    path('article_list_search/<int:pk>/', views.article_list_search, name='article_list_search'),
    path('', views.article_list, name='article_list'),
]