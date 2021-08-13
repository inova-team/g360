from django.urls import path
from event import views

urlpatterns = [
    path('event_upload/', views.event_upload, name="event_upload"),
    path('event_delete/<int:pk>', views.event_delete, name="event_delete"),
    path('event_update/<int:pk>', views.event_update, name="event_update"),
    path('event_list/', views.event_list, name="event_list"),
    path('event_detail/<int:pk>', views.event_detail, name="event_detail"),
]