from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('', views.renderHome, name="home"),
    path('contactenos/', views.renderContactUs_email,name="contact_us"),
    path('intranet/',views.renderIntranet,name="intranet"),
]