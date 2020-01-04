from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('wish/', views.wish_index, name='index'),
  path('wish/create/', views.WishCreate.as_view(), name='wish_create'),
  path('wish/<int:wish_id>/delete/', views.wish_delete, name='wish_delete'),

]