from django.urls import path
from . import views

urlpatterns = [
    path('cat_wallet/', views.getCatData),
]