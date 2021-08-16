from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('', views.render_home, name="home"),
    path('contactenos/', views.render_contact_us_email,name="contact_us"),
    path('intranet/',views.render_intranet,name="intranet"),
]