from django.urls import path
from . import views

urlpatterns = [
    path('cat-wallet/', views.getCatData),
]