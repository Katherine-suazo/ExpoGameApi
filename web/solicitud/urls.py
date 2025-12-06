from django.urls import path
from solicitud import views

urlpatterns = [
    path('', views.callGallery, name="solicitud"),
    path('category/<int:id_category>/',views.callCategory, name="category"),
]

