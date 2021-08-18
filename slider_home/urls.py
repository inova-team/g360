from django.urls import path
from slider_home import views

urlpatterns = [
    path('slider_upload/', views.slider_upload, name="slider_upload"),
    path('slider_delete/<int:pk>', views.slider_delete, name="slider_delete"),
    path('slider_update/<int:pk>', views.slider_update, name="slider_update"),
    path('slider_list/', views.slider_list, name="slider_list"),
    path('list_items_options/', views.list_items_options, name='list_items_options'),
]