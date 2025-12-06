from django.urls import path
from novedades import views

urlpatterns = [
path('',views.nov,name="novedades"),
]