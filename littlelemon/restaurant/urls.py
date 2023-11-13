from django.urls import path
from django.contrib import admin
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  path('', views.index, name="index"),
  
  # API link
  path('menu/', views.MenuItemView.as_view(), name="menu"),
  path('menu/<int:pk>', views.SingleMenuItem.as_view(), name="menu"),
  path('api-token-auth/', obtain_auth_token)
]