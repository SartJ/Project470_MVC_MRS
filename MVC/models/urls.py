from django.urls import path
from . import views

# URLS.py OF ACCOUNTS APP
app_name = "models"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout")
]
