from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  
  # API link
  path('menu/', views.MenuItemView.as_view(), name="menu"),
  path('menu/<int:pk>', views.SingleMenuItem.as_view(), name="menu"),
]