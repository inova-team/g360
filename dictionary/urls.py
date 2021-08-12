from django.contrib import admin
from django.urls import path
from dictionary import views

urlpatterns = [

    #word_category
    path('category_upload/', views.category_upload, name="category_create"),
    path('category_delete/<int:pk>/', views.category_delete, name="category_delete"),
    path('category_update/<int:pk>/', views.category_update, name="category_update"),
    path('', views.category_list, name="category_list"),

    #Word
    path('word_upload/', views.word_upload, name="word_upload"),
    path('word_delete/<int:pk>/', views.word_delete, name='word_delete'),
    path('word_update/<int:pk>/', views.word_update, name='word_update'),
    path('', views.word_list, name='word_list'),
]