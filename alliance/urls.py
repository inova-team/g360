from django.contrib import admin
from django.urls import path

from alliance import views

urlpatterns = [
    path('<int:pk>/', views.alliance_detail_user, name='alliance_detail_user'),
    path('', views.alliance_list_user, name='alliance_list_user'),
    path('alliance_list/', views.alliance_list, name='alliance_list'),
    path('alliance_upload/', views.alliance_upload, name="alliance_upload"),
    path('alliance_delete/<int:pk>/', views.alliance_delete, name='alliance_delete'),
    path('alliance_update/<int:pk>/', views.alliance_update, name='alliance_update'),
    # path('alliance_detail/<int:pk>/', views.alliance_detail, name='alliance_detail'),
    # path('alliance_list_search/<int:pk>/', views.alliance_list_search, name='alliance_list_search'),
]
