from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.plants_view),
    path('<int:id>', views.plants_view)
]
