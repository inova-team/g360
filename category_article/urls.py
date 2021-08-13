from django.contrib import admin
from django.urls import path
from category_article import views

urlpatterns = [
    path('category_upload/', views.category_upload, name="category_article_upload"),
    path('category_delete/<int:pk>/', views.category_delete, name="category_article_delete"),
    path('category_update/<int:pk>/', views.category_update, name="category_article_update"),
    path('', views.category_list, name="category_article_list"),
    path('category_articles/<int:pk>/', views.category_articles, name="category_article_articles"),
]