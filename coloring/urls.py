from django.urls import path
from . import views

urlpatterns = [
  path('archive/', views.archive, name='archive'),
    path('', views.index, name='index'), 
]