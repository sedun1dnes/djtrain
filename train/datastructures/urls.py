from django.urls import path, register_converter
from . import views, converters

register_converter(converters.Int3, 'int3')

urlpatterns = [
    path('', views.structures, name='home'),
    path('add_page/', views.add_page, name='add_page'),
    path('login/', views.login, name='login'),
    path('<int:num>/', views.datastructure, name='ds'),
]
