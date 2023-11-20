from django.urls import path
from . import  views

urlpatterns = [
    path("", views.user_page_view, name="user_page"),
    path("register/", views.user_register_view, name="register"),
    path("login/", views.user_log_in_view, name="login"),
    path("logout/", views.user_log_out_view, name="logout"),
]