from django.urls import path
from core import views

urlpatterns = [
    path('',views.home,name="home"),
    path('qsomos/',views.quienes_somos,name="qsomos"),
    path('lista/', views.listview, name='lista'),
    path('registro/usuario/', views.register_usuario, name='registro_usuario'),
    path('registro/cliente/', views.register_cliente, name='registro_cliente'),
]