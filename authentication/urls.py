from django.urls import path
from authentication import views

urlpatterns = [
    path('login/',views.renderLogin,name="g360Login"),
    path('register/',views.renderRegister,name="g360Register"),
    path('logout/',views.renderLogout,name="g360Logout"),
]